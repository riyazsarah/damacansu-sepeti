import http
import re
import secrets
import uuid
from datetime import datetime, timedelta
from typing import Tuple

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials
import jwt
from fastapi.security import HTTPBearer

security = HTTPBearer()


def decode_token(token, secret_key):
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload["data"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


async def get_current_user(
    token: HTTPAuthorizationCredentials = Depends(security),
    secret_key: str = "secret_key",
):
    try:
        payload = decode_token(token.credentials, secret_key)
        return payload
    except HTTPException as ex:
        raise ex


# Define a function to create a JWT token for a user
def jwt_encode(
    user_id: int,
    email: str = "example@gmail.com",
    password: str = "example123456#@",
    exp_time: any = datetime.utcnow() + timedelta(hours=24),
) -> tuple[str, str]:
    # Create the payload for the token
    payload = {"sub": user_id, "exp": exp_time, "email": email, "password": password}
    secret = secrets.token_hex(16)
    # Encode the payload as a JWT token using the secret key
    token = jwt.encode(payload, secret, algorithm="HS256")

    # Return the token as a string
    return token, secret


# Define a function to handle user sign up
def sign_up(email: str, password: str) -> Tuple[str, str]:
    # Check if the email is already in use
    # if email_already_exists(email):
    #    raise HTTPException(status_code=400, detail='Email address already in use')
    if is_email_valid(email):
        # Generate a unique ID for the new user
        user_id = uuid.uuid4().int

        # Generate a JWT token for the new user
        return jwt_encode(user_id, email, password)
    else:
        raise HTTPException(
            status_code=http.HTTPStatus.BAD_REQUEST, detail="email not valid"
        )


def is_email_valid(email: str):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True
