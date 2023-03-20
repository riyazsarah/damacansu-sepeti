import http
import re
import secrets
import uuid
from datetime import datetime, timedelta
from typing import Dict
from fastapi import HTTPException
import jwt
from passlib.handlers import bcrypt

from api.endpoints.database.models import UserDBModel


def jwt_decode(token: str, secret_key: str) -> Dict[str, any]:
    f"""
    Decodes and returns the payload. Raises exception if signature is expired or token is invalid.
    :param token: {str}
    :param secret_key: {str}
    :return: {Dict[str, any]}
    """
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail={
                "error": "Token has expired.",
                "timestamp": datetime.now().isoformat(),
            },
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail={"error": "Invalid token.", "timestamp": datetime.now().isoformat()},
        )


# Define a function to create a JWT token for a user
def jwt_account_encode(
    user_id: int,
    email: str = "example@gmail.com",
    password: str = "example123456#@",
    exp_time: datetime = datetime.utcnow() + timedelta(hours=24),
) -> Dict[str, any]:
    f"""
    Encodes the JWT with user_id, email, password and expiration time.
    :param user_id: {int}
    :param email: {str}
    :param password: {str}
    :param exp_time: {datetime} - Optional - Default => 24 hours from the moment jwt_encode is called
    :return: {Dict[str, any]} => OAuth 2 Token - Secret Token - Refresh Token in order
    """
    # Create the payload for the token
    payload = {
        UserDBModel.DBFields.USER_ID.value: user_id,
        "exp": exp_time,
        UserDBModel.DBFields.EMAIL.value: email,
        UserDBModel.DBFields.PASSWORD.value: password,
    }
    secret = secrets.token_hex(16)
    refresh_token = secrets.token_hex(16)
    # Encode the payload as a JWT token using the secret key
    token = jwt.encode(payload, secret, algorithm="HS256")
    # Return the token as a string
    return {
        UserDBModel.DBFields.ACCESS_TOKEN.value: token,
        UserDBModel.DBFields.SECRET_TOKEN.value: secret,
        UserDBModel.DBFields.REFRESH_TOKEN.value: refresh_token,
    }


def sign_up_handler(email: str, password: str, exp_time: datetime = datetime.utcnow() + timedelta(hours=24)) -> Dict[str, any]:
    f"""
    Generates an OAuth 2 and Secret token, with given email and passwords.
    :param exp_time: {datetime}
    :param email: {str}
    :param password:  {str}
    :return: {Dict[str, any]} => OAuth 2 Token - Secret Token - Refresh Token in order
    """
    # Check if the email is already in use
    # if email_already_exists(email):
    #    raise HTTPException(status_code=400, detail='Email address already in use')
    if is_email_valid(email):
        # Generate a unique ID for the new user
        user_id = uuid.uuid4().int

        # Generate a JWT token for the new user
        return jwt_account_encode(user_id, email, password, exp_time)
    else:
        raise HTTPException(
            status_code=http.HTTPStatus.BAD_REQUEST, detail="email not valid"
        )


def hash_and_salt_password(password: str) -> str:
    f"""
    Hashes and salts the password.
    :param password: {str}
    :return: {str} - Hashed and salted password
    """
    return bcrypt.bcrypt.hash(password)


def compare_plain_hashed_password(password: str, hashed_password: str) -> bool:
    f"""
    Checks if the password is valid. Returns true/false.
    :param password: {str}
    :param hashed_password: {str}
    :return: {bool}
    """
    return bcrypt.bcrypt.verify(password, hashed_password)


def is_email_valid(email: str):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True
