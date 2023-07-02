from marshmallow import ValidationError


class ErrShopNameNotUnique(Exception):
    def __init__(self, message: str = "shop name must be unique"):
        super().__init__(message)
