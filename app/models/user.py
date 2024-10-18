from sqlalchemy import Column, Integer, String

from app.core.database.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(length=255), index=True)
    email = Column(String(length=255), unique=True)
    password = Column(String(length=255))