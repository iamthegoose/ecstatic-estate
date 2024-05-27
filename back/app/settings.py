from typing import Optional

from pydantic import AnyUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: SecretStr
    DB_HOST: str
    DB_PORT: str

    model_config = SettingsConfigDict(
        env_file=('.env', 'stack.env'), env_file_encoding='utf-8', extra='ignore'
    )


settings = Settings()
