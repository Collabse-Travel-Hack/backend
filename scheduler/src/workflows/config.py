from pydantic import Field, MongoDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="", env_file=".env")
    cache_host: str = Field("158.160.14.223", alias="CACHE_HOST", env="REDIS_HOST")
    cache_port: int = Field("6379", alias="CACHE_PORT", env="CACHE_PORT")
    mongo_host: MongoDsn = Field(
        "mongodb://localhost:27017", alias="MONGO_HOST", env="MONGO_HOST"
    )
    elastic_host: str = Field(
        "http://158.160.14.223:9200", alias="ELASTIC_HOST", env="ELASTIC_HOST"
    )
    elastic_collection: str = Field(
        "places", alias="ELASTIC_COLLECTION", env="ELASTIC_COLLECTION"
    )
    timestamp_name: str = Field("latest", alias="TIMESTAMP_NAME", env="TIMESTAMP_NAME")
    batch_size: int = Field(10, alias="BATCH_SIZE", env="BATCH_SIZE")
    hatchet_client_token: str = Field(
        "eyJhbGciOiJFUzI1NiIsICJraWQiOiIwYTFvaWcifQ.eyJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCAiZXhwIjoxNzIwMjEwNDI2LCAiZ3JwY19icm9hZGNhc3RfYWRkcmVzcyI6ImxvY2FsaG9zdDo3MDc3IiwgImlhdCI6MTcxMjQzNDQyNiwgImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsICJzZXJ2ZXJfdXJsIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwIiwgInN1YiI6IjcwN2QwODU1LTgwYWItNGUxZi1hMTU2LWYxYzQ1NDZjYmY1MiIsICJ0b2tlbl9pZCI6ImNlYmMyM2M5LWZhMjctNGJlYy1hZjY4LTE0NjBjMDBhNGRlNyJ9.MkwdhabsoXPovcmbGMkHp20shC7SJig8i-xLwEqI7AIh_vcaxnVubTCDAmu-Zo8Z9VTzyVqLmsz1b-Ysc43r-Q",
        alias="HATCHET_CLIENT_TOKEN",
    )
    mongo_database: str = Field("storage", alias="MONGO_DATABASE", env="MONGO_DATABASE")
    mongo_collection: str = Field(
        "all_objects", alias="MONGO_COLLECTION", env="MONGO_COLLECTION"
    )


settings = Settings()
