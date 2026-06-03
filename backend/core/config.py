from functools import lru_cache

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "SENTINEL"

    API_PREFIX: str = "/api/v1"

    POSTGRES_HOST: str = "localhost"

    POSTGRES_PORT: int = 5434

    POSTGRES_DB: str = "sentinel"

    POSTGRES_USER: str = "sentinel"

    POSTGRES_PASSWORD: str = "sentinel"

    DATABASE_ECHO: bool = False

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )

    @property
    def database_url(self) -> str:
        return (
            "postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )


@lru_cache
def get_settings():
    return Settings()