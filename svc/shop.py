import uuid
from model.shop import Shop
from sqlalchemy import Connection as DBConnection


class ShopDAL:
    def __init__(self, db_connection: DBConnection):
        self.db_connection = db_connection

    def store(self, shop: Shop) -> Shop:
        pass

    def fetch(self, shop_id: uuid.UUID) -> Shop:
        pass

    def fetch_by_user_id(self, user_id: uuid.UUID) -> list[Shop]:
        pass
