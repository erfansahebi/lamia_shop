from concurrent.futures import ThreadPoolExecutor
from sys import argv
from grpc import server as grpc_server
from handler.shop import ShopService
from handler.common import Handler
from di.container import DIContainer
from config.config import Config
from lamia_shared.proto.shop.shop_pb2_grpc import add_ShopServiceServicer_to_server


def main() -> None:
    cmd = argv[-1]

    if cmd == "main.py":
        print("None")
    elif cmd == "serve":
        print("hello")
        server = grpc_server(thread_pool=ThreadPoolExecutor(max_workers=10))
        handler = Handler(di=DIContainer(config=Config()))
        add_ShopServiceServicer_to_server(servicer=ShopService(handler=handler), server=server)
        server.add_insecure_port(address='[::]:50053')
        server.start()
        server.wait_for_termination()


if __name__ == '__main__':
    main()
