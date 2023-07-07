from di.container import DIContainer


class RequestSchema:
    def __init__(self, request: dict):
        self.request = request

    def validate(self, di: DIContainer) -> None:
        pass
