import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="", env_file=".env")
    project_name: str = Field(
        "ETL Kafka в ClickHouse", alias="PROJECT_NAME", env="PROJECT_NAME"
    )
    description: str = Field(
        "Загрузка данных из Kafka в ClickHouse",
        alias="DESCRIPTION",
        env="DESCRIPTION",
    )

    CH_HOST: str = Field("localhost", alias="CH_HOST", env="CH_HOST")
    CH_PORT: int = Field(9000, alias="CH_PORT", env="CH_PORT")

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
    KAFKA_HOST: str = Field("localhost", alias="KAFKA_HOST", env="KAFKA_HOST")
    KAFKA_PORT: int = Field(9094, alias="KAFKA_PORT", env="KAFKA_PORT")
    KAFKA_GROUP: str = Field("events", alias="KAFKA_PORT", env="KAFKA_GROUP")

    base_dir: str = os.path.dirname(os.path.abspath(__file__))


settings = Settings()
