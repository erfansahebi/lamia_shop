from di.container import DIContainer
from marshmallow import Schema, fields
from schema.shop import ShopSchema


class CreateSchema(Schema):
    user_id = fields.UUID()
    name = fields.Str()


class Create:
    def __init__(self, request: dict):
        self.request = request

    def validate(self, di: DIContainer) -> None:
        self.schema = CreateSchema().load(
            data={
                'user_id': self.request.shop.user_id,
                'name': self.request.shop.name,
            }
        )

        if (di.get_shop_dal()).check_exist_by_user_id(user_id=self.schema['user_id']):
            raise Exception('shop for user exists')

        ss = ShopSchema().dump(self.schema)

        (di.get_shop_dal()).store(shop=ss)

        return
