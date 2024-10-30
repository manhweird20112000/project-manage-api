from enum import Enum

from app import Base
from app.core.database.mixin import TrackTimeMixin

from sqlalchemy import Column, Integer, String, Enum as SqlEnum, SmallInteger


class ERole(Enum):
    system = 1,
    supper_admin = 2
    admin = 3
    viewer = 4
    editor = 5


class Admin(Base, TrackTimeMixin):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(length=64))

    email = Column(String(length=128), unique=True)

    password = Column(String(length=255))

    avatar_url = Column(String(length=255), nullable=True)

    role = Column(SqlEnum(ERole), default=ERole.admin)

    status = Column(SmallInteger, default=1)
