from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from database.models import Shop


class ShopSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Shop
        include_relationships = True
        load_instance = True
