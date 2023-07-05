import grpc
from lamia_shared.proto.shop import shop_pb2, shop_pb2_grpc
from .common import Handler
from .validator import shop as shop_validator
from marshmallow import ValidationError


class ShopService(shop_pb2_grpc.ShopServiceServicer):

    def __init__(self, handler: Handler):
        self.handler = handler

    def Create(self, request, context):

        pend_data = shop_validator.Create(request=request)

        try:
            pend_data.validate(di=self.handler.di)
        except ValidationError as err:
            print(err)
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(err))

        return shop_pb2.CreateResponse(
            shop=shop_pb2.ShopStruct(
                id=str(pend_data.schema['id']),
                user_id=str(pend_data.schema['user_id']),
                name=pend_data.schema['name'],
            )
        )

    def Get(self, request, context):
        pass

    def GetByUserID(self, request, context):
        pass
