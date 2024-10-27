from sqlalchemy import String, DateTime, Column, Integer

from app import Base


class TokenBlackList(Base):
    __tablename__ = 'token_blacklist'

    id = Column(Integer, autoincrement=True, nullable=False, unique=True, primary_key=True)
    token = Column(String(255), unique=True, index=True)
    expires_at = Column(DateTime)