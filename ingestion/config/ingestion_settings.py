from pydantic_settings import BaseSettings


class IngestionSettings(BaseSettings):

    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"

    PROMETHEUS_URL: str = "http://localhost:9090"

    LOKI_URL: str = "http://localhost:3100"

    JAEGER_URL: str = "http://localhost:16686"

    REDIS_URL: str = "redis://localhost:6379"

    class Config:
        env_file = ".env"


settings = IngestionSettings()