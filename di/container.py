from sqlalchemy import Connection as DBConnection
from svc.shop import ShopDAL
from config.config import Config


class DIContainer:
    def __init__(self, config: Config):
        self.config = config

    def shop_dal(self) -> ShopDAL:
        self.__init_shop_dal()

        return self.shop_dal

    def __init_shop_dal(self) -> None:
        if hasattr(self, 'shop_dal'):
            return None

        self.shop_dal = ShopDAL(db_connection=self.__get_postgres_connection())
        return

    def __get_postgres_connection(self) -> DBConnection:
        self.__init_postgres()

        return self.postgres_connection

    def __init_postgres(self) -> None:
        if hasattr(self, 'postgres_connection'):
            return

        self.postgres_connection = sqlalchemy.create_engine(
            url=sqlalchemy.URL(
                drivername="postgresql",
                username=self.config.Database.Username,
                password=self.config.Database.Password,
                host=self.config.Database.Host,
                port=self.config.Database.Port,
                database=self.config.Database.Name,
            ),
        ).connect()

        return
