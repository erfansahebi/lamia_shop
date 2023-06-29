from lamia_shared.proto.shop import shop_pb2, shop_pb2_grpc
from common import Handler


class ShopService(shop_pb2_grpc.ShopServiceServicer):

    def __init__(self, handler: Handler):
        self.handler = handler

    def Create(self, request, context):
        return shop_pb2.ServerServicer()
        pass

    def Get(self, request, context):
        pass

    def GetByUserID(self, request, context):
        pass
