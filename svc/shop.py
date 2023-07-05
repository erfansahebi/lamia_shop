import uuid
from schema.shop import ShopSchema
from sqlalchemy.sql import exists
from database.models import Shop


class ShopDAL:
    def __init__(self, db_session):
        self.db_session = db_session

    def store(self, shop: ShopSchema) -> ShopSchema:
        print(shop['user_id'])
        pass

    def fetch(self, shop_id: uuid.UUID) -> ShopSchema:
        pass

    def fetch_by_user_id(self, user_id: uuid.UUID) -> list[ShopSchema]:
        pass

    def check_exist_by_user_id(self, user_id: uuid.UUID) -> bool:
        return self.db_session.query(exists().where(Shop.user_id == user_id)).scalar()
