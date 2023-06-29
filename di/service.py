from lamia_shop.config.config import Config


class ShopServiceInterface:
    def configuration(self) -> Config:
        pass

    def client(self):
        pass


class ShopService(ShopServiceInterface):
    def __init__(self, config: Config):
        self.config = config

    def configuration(self) -> Config:
        return self.config

    def client(self):
        print("client")
