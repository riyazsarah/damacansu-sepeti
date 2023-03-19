import http
from datetime import datetime

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorCollection
from starlette.responses import JSONResponse

from api.endpoints.auth.auth import sign_up
from api.models.users import UserToken, UserSignup, UserLogin, UserAuthFailed
from database.models import UserDBModel
from database.connect import get_db, users_db, users_collection

router = APIRouter(prefix="/user")


@router.post(
    "/signup",
    response_description="Returns Bearer OAuth 2 token.",
    response_model=UserToken,
)
async def create_access_token(
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
    :return:
    """
    jwt_token, jwt_secret = sign_up(
        email=user_details.email, password=user_details.password
    )

    response_struct = UserToken()
    db_struct = UserDBModel()
    db_struct.access_token = response_struct.access_token = jwt_token
    db_struct.secret_token = response_struct.secret_token = jwt_secret
    db_struct.token_type = response_struct.token_type = "bearer"
    db_struct.expires_in = response_struct.expires_in = 3600
    db_struct.email = user_details.email
    db_struct = jsonable_encoder(db_struct)
    await db.insert_one(db_struct)
    return JSONResponse(
        status_code=http.HTTPStatus.CREATED, content=response_struct.dict()
    )


@router.post(
    "/login",
    response_description="Logins with Bearer OAuth 2 token and Secret token.",
    response_model=UserToken,
    responses={
        400: {
            "model": UserAuthFailed,
            "description": "Invalid credentials or user not found.",
        }
    }
)
async def login(
    user_details: UserLogin = Body(...),
    db: AsyncIOMotorCollection = Depends(
        get_db(database_name=users_db, collection_name=users_collection)
    ),
):
    user_credentials = await db.find_one({"access_token": user_details.access_token})
    if user_credentials:
        user_credentials_dict = dict(user_credentials)
        if user_credentials_dict.get("secret_token") == user_details.secret_token:
            return UserToken(
                access_token=user_credentials_dict.get("access_token"),
                secret_token=user_credentials_dict.get("secret_token"),
                token_type=user_credentials_dict.get("token_type"),
                expires_in=user_credentials_dict.get("expires_in"),
            )
        else:
            return JSONResponse(
                status_code=http.HTTPStatus.BAD_REQUEST,
                content={
                    "error": "invalid secret token",
                    "timestamp": datetime.now().isoformat(),
                }
            )
    else:
        return JSONResponse(
            status_code=http.HTTPStatus.BAD_REQUEST,
            content={
                "error": "no user found with the specified access token",
                "datetime": datetime.now().isoformat(),
            }
        )
