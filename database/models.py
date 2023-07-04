from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, UUID
from datetime import datetime
from config.config import Config

Base = declarative_base()
metadata = Base.metadata


def get_sql_alchemy_url(config: Config) -> str:
    return 'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'.format(
        db_user=config.Database.Username,
        db_password=config.Database.Password,
        db_host=config.Database.Host,
        db_port=config.Database.Port,
        db_name=config.Database.Name,
    )


class Shop(Base):
    __tablename__ = 'shops'

    id = Column(UUID, primary_key=True)
    user_id = Column(UUID)
    name = Column(String(255))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
