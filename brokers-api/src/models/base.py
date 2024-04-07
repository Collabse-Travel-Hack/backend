import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class BaseEvent(BaseModel):
    account_id: UUID | None = None
    author_id: UUID | None = None
    event_type: str | None = None
    user_agent: str | None = None
    product_id: UUID | None = None
    timestamp: datetime.datetime = Field(default=datetime.datetime.now(datetime.UTC))
