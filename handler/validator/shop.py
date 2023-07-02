from di.container import DIContainer
from model.shop import Shop


class Create:
    def __init__(self, request: dict):
        self.request = request

    def validate(self, di: DIContainer) -> None:
        self.shop = Shop().load(
            data={
                'user_id': self.request.shop.user_id,
                'name': self.request.shop.name,
            }
        )
