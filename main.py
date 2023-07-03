import pprint
from concurrent.futures import ThreadPoolExecutor
from sys import argv
from grpc import server as grpc_server
from handler.shop import ShopService
from handler.common import Handler
from di.container import DIContainer
from config.config import Config
from lamia_shared.proto.shop.shop_pb2_grpc import add_ShopServiceServicer_to_server
import logging as log


def main() -> None:
    cmd = argv[-1]

    log.basicConfig(
        level=log.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    log.info('Starting with command: {command}'.format(command=cmd))

    if cmd == 'main.py':
        log.error('Empty command')
    elif cmd == 'migrate':
        print('migrate')
    elif cmd == 'serve':
        config = Config()
        server = grpc_server(thread_pool=ThreadPoolExecutor(max_workers=config.Server.MaxWorkers))
        handler = Handler(di=DIContainer(config=config))
        add_ShopServiceServicer_to_server(servicer=ShopService(handler=handler), server=server)
        server.add_insecure_port(address='{host}:{port}'.format(host=config.HTTP.Host, port=config.HTTP.Port))
        server.start()
        server.wait_for_termination()


if __name__ == '__main__':
    main()
