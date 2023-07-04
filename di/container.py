import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
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
            return

        self.shop_dal = ShopDAL(db_connection=self.__get_db_connection())
        return

    def __get_db_session(self):
        self.__init_db_session()

        return self.db_session

    def __init_db_session(self) -> None:
        if hasattr(self, 'db_session'):
            return

        self.db_session = scoped_session(
            session_factory=sessionmaker(
                bind=self.__get_db_connection(),
            )
        )

    def __get_db_connection(self) -> sqlalchemy.Connection:
        self.__init_db_connection()

        return self.db_connection

    def __init_db_connection(self) -> None:
        if hasattr(self, 'db_connection'):
            return

        self.db_connection = sqlalchemy.create_engine(
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
