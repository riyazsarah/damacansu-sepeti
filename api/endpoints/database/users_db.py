import http
from datetime import datetime

import jwt
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorCollection
from starlette.responses import JSONResponse

from api.auth.auth import (
    sign_up_handler,
    jwt_decode,
    jwt_account_encode,
    hash_and_salt_password,
    compare_plain_hashed_password,
)
from api.models.users import (
    UserToken,
    UserSignup,
    UserLogin,
    UserAuthFailed,
    RefreshTokenEndpoint,
)
from api.endpoints.database.models import UserDBModel
from api.endpoints.database.connect import get_db, users_db, users_collection

router = APIRouter(prefix="/user")


@router.post(
    "/signup",
    response_description="Returns Bearer OAuth 2 token.",
    response_model=UserToken,
    responses={
        400: {"model": UserAuthFailed},
    },
)
async def sign_up(
    user_details: UserSignup = Body(...),
    db: AsyncIOMotorCollection = Depends(
        get_db(database_name=users_db, collection_name=users_collection)
    ),
):
    f"""
    Creates a new access and secret token for the user.
    TODO: Seperate secret token creation from access token creation.
    :param user_details: {UserSignup}
    :param db:  {AsyncIOMotorCollection}
    :return: {UserToken}
    """
    tokens = sign_up_handler(email=user_details.email, password=user_details.password)
    # assure that user not yet signed up
    user_credentials = await db.find_one(
        {UserDBModel.DBFields.EMAIL.value: user_details.email}
    )
    # if they did already
    if user_credentials is not None:
        # check if their auth token is still valid, if it is not, error will be raised.
        expiration_time = jwt_decode(
            dict(user_credentials).get(UserDBModel.DBFields.ACCESS_TOKEN.value),
            dict(user_credentials).get(UserDBModel.DBFields.SECRET_TOKEN.value),
        ).get("exp")
        # convert unix timestamp to datetime
        expiration_time = datetime.fromtimestamp(expiration_time.get("exp"))
        # calculate the time difference between now and the expiration time.
        time_difference = expiration_time - datetime.now()
        return JSONResponse(
            status_code=http.HTTPStatus.BAD_REQUEST,
            content={
                "error": "User already exists.",
                "message": "Key will expire in {} hours, {} minutes and {} seconds."
                + " You can use /refresh_auth endpoint with your refresh token if you want to reset your OAuth 2 token.".format(
                    time_difference.seconds // 3600,
                    (time_difference.seconds // 60) % 60,
                    time_difference.seconds % 60,
                ),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            },
        )
    db_struct = return_db_struct(tokens, user_details)
    await db.insert_one(db_struct)
    return JSONResponse(
        status_code=http.HTTPStatus.CREATED,
        content={
            UserDBModel.DBFields.ACCESS_TOKEN.value: db_struct.access_token,
            UserDBModel.DBFields.SECRET_TOKEN.value: db_struct.secret_token,
            UserDBModel.DBFields.REFRESH_TOKEN.value: db_struct.refresh_token,
            UserDBModel.DBFields.TOKEN_TYPE.value: db_struct.token_type,
        },
    )


def return_db_struct(tokens: dict, user_details: UserSignup) -> UserDBModel:
    f"""
    Returns the response and updates the database with the new tokens.
    Password is hashed on the way.
    :param user_details: {UserSignup}
    :param tokens: {dict} -> Contains the access, secret and refresh tokens.
    :return: {UserDBModel} -> Returns the client response and the database structure, in order.
    """
    db_struct = UserDBModel()
    db_struct.access_token = tokens.get(UserDBModel.DBFields.ACCESS_TOKEN.value)
    db_struct.secret_token = tokens.get(UserDBModel.DBFields.SECRET_TOKEN.value)
    db_struct.refresh_token = tokens.get(UserDBModel.DBFields.REFRESH_TOKEN.value)
    db_struct.token_type = "bearer"
    db_struct.email = user_details.email
    db_struct.password = hash_and_salt_password(user_details.password)
    db_struct = jsonable_encoder(db_struct)
    return db_struct


@router.post(
    "/refresh_auth",
    response_description="Refreshes the access token with the given OAuth 2 token, refresh token and secret token.",
    response_model=UserToken,
    responses={
        400: {"model": UserAuthFailed},
    },
)
async def refresh_auth(
    user_details: RefreshTokenEndpoint = Body(...),
    db: AsyncIOMotorCollection = Depends(
        get_db(database_name=users_db, collection_name=users_collection)
    ),
):
    user_details_dict = dict(user_details)
    db_fields = UserDBModel.DBFields
    # this will already handle if the token is expired or not.
    payload = jwt.decode(
        user_details_dict.get(db_fields.ACCESS_TOKEN.value),
        user_details_dict.get(db_fields.SECRET_TOKEN.value),
        algorithms=["HS256"],
    )
    # if we are here, the token is valid. generate new tokens.
    new_access_token = jwt_account_encode(
        payload.get(db_fields.USER_ID.value),
        payload.get(db_fields.EMAIL.value),
        payload.get(db_fields.PASSWORD.value),
    )
    # match the email in the payload with the email in the database.
    # and also match refresh token that is supplied.
    result = await db.update_one(
        {
            "$and": [
                {
                    db_fields.ACCESS_TOKEN.value: dict(payload).get(
                        db_fields.EMAIL.value
                    )
                },
                {
                    db_fields.REFRESH_TOKEN.value: user_details_dict.get(
                        db_fields.REFRESH_TOKEN.value
                    )
                },
            ]
        },
        {"$set": {db_fields.ACCESS_TOKEN.value: new_access_token}},
    )
    if result.count_documents({}) == 0:
        raise HTTPException(
            status_code=http.HTTPStatus.BAD_REQUEST,
            detail="Invalid refresh token.",
        )
    response_struct = UserToken()
    response_struct.secret_token = user_details_dict.get(db_fields.SECRET_TOKEN.value)
    response_struct.refresh_token = user_details_dict.get(db_fields.REFRESH_TOKEN.value)
    response_struct.access_token = new_access_token
    response_struct.token_type = "bearer"
    return JSONResponse(
        status_code=http.HTTPStatus.OK, content=jsonable_encoder(response_struct)
    )


@router.post(
    "/login",
    response_description="Logins with Bearer OAuth 2 token and Secret token.",
    response_model=UserToken,
)
async def login(
    user_details: UserLogin = Body(...),
    db: AsyncIOMotorCollection = Depends(
        get_db(database_name=users_db, collection_name=users_collection)
    ),
):
    f"""
    Logins with Bearer OAuth 2 token and Secret token.
    :param user_details: {UserLogin}
    :param db: {AsyncIOMotorCollection}
    :return: {UserToken}
    """
    db_fields = UserDBModel.DBFields
    user_credentials = await db.find_one(
        {db_fields.ACCESS_TOKEN.value: user_details.access_token}
    )
    if user_credentials:
        user_credentials_dict = dict(user_credentials)
        # we don't care about the payload for now, just check if the token is not expired,
        # and if the secret token is valid.
        payload = jwt_decode(
            user_credentials_dict.get(db_fields.ACCESS_TOKEN.value),
            user_credentials_dict.get(db_fields.SECRET_TOKEN.value),
        )
        # if yes, we are not done yet! payload carries the plain password.
        # and user_credentials_dict carries the hashed password.
        # compare em! juust for a bit extra security. probably unnecessary. but whatever.
        if compare_plain_hashed_password(
            dict(payload).get(db_fields.PASSWORD.value),
            user_credentials_dict.get(db_fields.PASSWORD.value),
        ):
            return UserToken(
                access_token=user_credentials_dict.get(db_fields.ACCESS_TOKEN.value),
                secret_token=user_credentials_dict.get(db_fields.SECRET_TOKEN.value),
                token_type=user_credentials_dict.get(db_fields.TOKEN_TYPE.value),
            )
        else:
            return JSONResponse(
                status_code=http.HTTPStatus.BAD_REQUEST,
                content={
                    "error": "User credentials are invalid.",
                    "message": "Please check your access token and secret token.",
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                },
            )
    else:
        return JSONResponse(
            status_code=http.HTTPStatus.BAD_REQUEST,
            content={
                "error": "no user found with the specified access token",
                "datetime": datetime.now().isoformat(),
            },
        )
