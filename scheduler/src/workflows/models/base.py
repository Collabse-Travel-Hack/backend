import datetime

from pydantic import BaseModel, Field


class BaseDataModel(BaseModel):
    id: str
    timestamp: datetime.datetime | None = Field(
        default=datetime.datetime.now(datetime.UTC)
    )

    class Config:
        from_attributes = True
