from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, TIMESTAMP, text, DateTime, UUID
from datetime import datetime

Base = declarative_base()
metadata = Base.metadata


class Shop(Base):
    __tablename__ = 'shops'

    id = Column(UUID, primary_key=True)
    user_id = Column(UUID)
    name = Column(String(255))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)