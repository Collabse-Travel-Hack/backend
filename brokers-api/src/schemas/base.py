import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class BaseEventSchema(BaseModel):
    author_id: UUID | None = None
    event_type: str | None = None
    product_id: UUID
    timestamp: datetime.datetime = Field(default=datetime.datetime.now(datetime.UTC))
