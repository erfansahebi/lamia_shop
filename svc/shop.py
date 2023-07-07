import uuid
from schema.shop import ShopSchema
from sqlalchemy.sql import exists
from database.models import Shop


class ShopDAL:
    def __init__(self, db_session):
        self.db_session = db_session

    def store(self, shop: ShopSchema) -> ShopSchema:
        stored_shop = Shop(
            id=uuid.uuid4(),
            user_id=shop['user_id'],
            name=shop['name'],
        )

        self.db_session.add(stored_shop)
        self.db_session.commit()

        shop_schema = ShopSchema()

        return shop_schema.dump(obj=stored_shop)

    def fetch(self, shop_id: uuid.UUID) -> ShopSchema | None:
        fetched_shop = self.db_session.query(Shop).filter(Shop.id == shop_id).one_or_none()
        if fetched_shop:
            shop_schema = ShopSchema()
            return shop_schema.dump(obj=fetched_shop)

        return

    def check_exist_by_user_id(self, user_id: uuid.UUID) -> bool:
        return self.db_session.query(exists().where(Shop.user_id == user_id)).scalar()
