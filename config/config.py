from os import environ as env


class Config:

    def __init__(self):
        self.HTTP = HTTP()
        self.Server = Server()


class HTTP:
    Host: str
    Port: str

    def __init__(self):
        self.Host = env['HOST']
        self.Port = env['PORT']


class Server:
    MaxWorkers: int

    def __init__(self):
        self.MaxWorkers = int(env['MAX_WORKERS'])
