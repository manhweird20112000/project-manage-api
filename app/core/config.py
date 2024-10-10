import secrets
import os
from dotenv import load_dotenv
from pydantic import computed_field
from pydantic.v1 import BaseSettings
from pydantic_core import MultiHostUrl

load_dotenv()

class Settings(BaseSettings):
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
    def SQLALCHEMY_DATABASE_URI(self):
        return MultiHostUrl.build(
            scheme="mysql+pymysql",
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT,
            path=self.DB_NAME
        )


settings = Settings()