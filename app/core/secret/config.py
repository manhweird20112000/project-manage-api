import secrets
import os
from dotenv import load_dotenv
from pydantic import BaseModel, computed_field

load_dotenv()

class Settings(BaseModel):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    DB_HOST: str = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT: int = os.getenv("DB_PORT", "3306")
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_NAME: str = os.getenv("DB_NAME")

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f'mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


settings = Settings()