import logging
from pathlib import Path

import backoff
from aiohttp import ClientConnectorError
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from src.exceptions.rate import RateLimitException
from src.rate.rate_limiter import is_circuit_processable


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="", env_file=".env")
    project_name: str = Field(
        "API для общения с брокером сообщений",
        alias="PROJECT_NAME",
        env="PROJECT_NAME",
    )
    description: str = Field(
        "Отправка и чтение сообщений в/из очереди",
        alias="DESCRIPTION",
        env="DESCRIPTION",
    )
    service_name: str = Field("broker-api", alias="SERVICE_NAME", env="SERVICE_NAME")
    version: str = Field("1.0.0", alias="VERSION", env="VERSION")
    base_dir: str = str(Path(__file__).parent.parent)
    profile_route: str = Field(
        "auth-api:8000/api/v1/users", alias="PROFILE_ROUTE", env="PROFILE_ROUTE"
    )
    bootstrap_servers: str = Field(
        "158.160.14.223:9094", alias="BOOTSTRAP_SERVERS", env="BOOTSTRAP_SERVERS"
    )
    client_id: str = Field("broker_service", alias="CLIENT_ID", env="CLIENT_ID")
    auto_offset_reset: str = Field(
        "earliest", alias="AUTO_OFFSET_RESET", env="AUTO_OFFSET_RESET"
    )
    enable_auto_commit: bool = Field(
        False, alias="ENABLE_AUTO_COMMIT", env="ENABLE_AUTO_COMMIT"
    )
    retry_backoff_ms: int = Field(500, alias="RETRY_BACKOFF_MS", env="RETRY_BACKOFF_MS")
    kafka_seen_media_topic: str = Field(
        "seen_medias", alias="KAFKA_SEEN_MEDIA_TOPIC", env="KAFKA_SEN_MEDIA_TOPIC"
    )
    kafka_click_topic: str = Field(
        "clicks", alias="KAFKA_CLICK_TOPIC", env="KAFKA_CLICK_TOPIC"
    )
    kafka_bookmark_topic: str = Field(
        "likes", alias="KAFKA_LIKE_TOPIC", env="KAFKA_LIKE_TOPIC"
    )
    kafka_buy_topic: str = Field(
        "buys", alias="KAFKA_BUY_TOPIC", env="KAFKA_BUYS_TOPIC"
    )
    kafka_commented_topic: str = Field(
        "commented", alias="KAFKA_COMMENTED_TOPIC", env="KAFKA_COMMENTED_TOPIC"
    )
    kafka_uploaded_topic: str = Field(
        "media-uploaded", alias="KAFKA_UPLOAD_TOPIC", env="KAFKA_UPLOAD_TOPIC"
    )
    jaeger_host: str = Field(
        "jaeger-collector:12497", alias="JAEGER_HOST", env="JAEGER_HOST"
    )

    backoff_max_retries: int = Field(
        5, alias="BACKOFF_MAX_RETRIES", env="BACKOFF_MAX_RETRIES"
    )
    enable_tracer: bool = Field(False, alias="ENABLE_TRACER", env="ENABLE_TRACER")


settings = Settings()
logger = logging.getLogger(__name__)
BACKOFF_CONFIG = {
    "wait_gen": backoff.expo,
    "exception": (ClientConnectorError, RateLimitException),
    "logger": logger,
    "max_tries": settings.backoff_max_retries,
}

CIRCUIT_CONFIG = {"expected_exception": is_circuit_processable}
