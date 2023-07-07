from di.container import DIContainer
from marshmallow import Schema, fields
from .common import RequestSchema


class CreateSchema(Schema):
    user_id = fields.UUID()
    name = fields.Str()


class Create(RequestSchema):
    def validate(self, di: DIContainer) -> None:
        self.schema = CreateSchema().load(
            data={
                'user_id': self.request.shop.user_id,
                'name': self.request.shop.name,
            }
        )

        if (di.get_shop_dal()).check_exist_by_user_id(user_id=self.schema['user_id']):
            raise Exception('shop for user exists')

        return


class GetSchema(Schema):
    id = fields.UUID()


class Get(RequestSchema):
    def validate(self, di: DIContainer) -> None:
        self.schema = GetSchema().load(
            data={
                'id': self.request.id,
            },
        )

        self.fetched_shop = di.get_shop_dal().fetch(shop_id=self.schema['id'])
        if self.fetched_shop is None:
            raise Exception("shop doesn't exists")

        return
