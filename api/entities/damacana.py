from abc import ABC


class Damacana(ABC):
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        image: str,
        price: float = 15.99,
        quantity: int = 0,
    ):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.image = image

    @property
    def get_id(self):
        return self.id

    @property
    def get_name(self):
        return self.name

    @property
    def get_price(self):
        return self.price

    @property
    def get_quantity(self):
        return self.quantity

    @property
    def get_description(self):
        return self.description

    @property
    def get_image(self):
        return self.image
