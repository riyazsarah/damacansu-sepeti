from abc import ABC
from typing import Union
from pydantic import BaseModel


class DamacanaGeneralModel(ABC, BaseModel):
    id: str
    name: str
    description: Union[str, None]
    image: Union[str, None]
    price: float = 15.99
    quantity: int = 0
