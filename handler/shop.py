import grpc
from lamia_shared.proto.shop import shop_pb2, shop_pb2_grpc
from .common import Handler
from .validator import shop as shop_validator


class ShopService(shop_pb2_grpc.ShopServiceServicer):

    def __init__(self, handler: Handler):
        self.handler = handler

    def Create(self, request, context):
        pend_data = shop_validator.Create(request=request)

        try:
            pend_data.validate(di=self.handler.di)
        except Exception as err:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(err))

        created_shop = self.handler.di.get_shop_dal().store(pend_data.schema)

        return shop_pb2.CreateResponse(
            shop=shop_pb2.ShopStruct(
                id=str(created_shop['id']),
                user_id=str(created_shop['user_id']),
                name=created_shop['name'],
            )
        )

    def Get(self, request, context):
        pend_data = shop_validator.Get(request=request)

        try:
            pend_data.validate(di=self.handler.di)
        except Exception as err:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(err))

        return shop_pb2.CreateResponse(
            shop=shop_pb2.ShopStruct(
                id=str(pend_data.fetched_shop['id']),
                user_id=str(pend_data.fetched_shop['user_id']),
                name=pend_data.fetched_shop['name'],
            )
        )
