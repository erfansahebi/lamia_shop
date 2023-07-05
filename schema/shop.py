from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from database.models import Shop


class ShopSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Shop
        load_instance = True

    id = auto_field()
    user_id = auto_field()
    name = auto_field()
    created_at = auto_field()
    updated_at = auto_field()
