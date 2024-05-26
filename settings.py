from typing import Optional

from pydantic import AnyUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    REDIS_HOST: SecretStr
    REDIS_PORT: int
    API_ACCESS_TOKEN: SecretStr
    IMGUR_CLIENT_ID: str
    IMGUR_CLIENT_SECRET: str

    model_config = SettingsConfigDict(
        env_file=('.env', 'stack.env'), env_file_encoding='utf-8', extra='ignore'
    )


settings = Settings()