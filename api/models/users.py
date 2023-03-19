from abc import ABC
from datetime import datetime

from pydantic import Field

from pydantic import BaseModel


class UserSignup(ABC, BaseModel):
    email: str
    password: str


class UserLogin(ABC, BaseModel):
    access_token: str
    secret_token: str


class UserToken(ABC, BaseModel):
    access_token: str | None = Field("", description="User Access Token")
    secret_token: str | None = Field("", description="User Secret Token")
    token_type: str | None = Field("", description="Bearer, or whatever.")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEzMjcxMjgyMDIxMzkyNzM2MTY1MDEwNTAyODc3N",
                "secret_token": "ec6e3c68bbf1869e60a16d10a200e23d",
                "token_type": "bearer",
            }
        }

class UserAuthFailed(ABC, BaseModel):
    error: str = Field("no error, yet.", description="Error Message")
    timestamp: datetime = Field(datetime.now().isoformat(), description="Timestamp")

    class Config:
        schema_extra = {
            "example": {
                "error": "invalid secret token",
                "timestamp": datetime.now().isoformat(),
            }
        }