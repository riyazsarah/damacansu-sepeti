from datetime import datetime, timedelta

from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Union
from enum import Enum

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class DamacanaDBModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(..., description="Damacana Name")
    description: str = Field(..., description="Damacana Description")
    image: str = Field(..., description="Damacana Image")
    price: float = Field(15.99, description="Damacana Price")
    quantity: int = Field(0, description="Damacana Quantity")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Erikli 19 Liter",
                "description": "Erikli 19 Liter Damacana",
                "image": "https://www.example.com/image.jpg",
                "price": 23.99,
                "quantity": 30,
            }
        }
    class DBFields(Enum):
        ID = "_id"
        NAME = "name"
        DESCRIPTION = "description"
        IMAGE = "image"
        PRICE = "price"
        QUANTITY = "quantity"




class UpdateDamacanaModel(BaseModel):
    name: Union[str, None]
    description: Union[str, None]
    image: Union[str, None]
    price: Union[float, None]
    quantity: Union[int, None]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": "123",
                "name": "Erikli 19 Liter",
                "description": "Erikli 19 Liter Damacana",
                "image": "https://www.example.com/image.jpg",
                "price": 23.99,
                "quantity": 30,
            }
        }


class UserDBModel (BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    access_token: str = Field("", description="User Access Token")
    secret_token: str = Field("", description="User Secret Token")
    token_type: str = Field("", description="Bearer")
    email: str = Field("", description="User Email")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    class DBFields(Enum):
            ID = "_id"
            ACCESS_TOKEN = "access_token"
            SECRET_TOKEN = "secret_token"
            TOKEN_TYPE = "token_type"
            EMAIL = "email"
