import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class BaseEventSchema(BaseModel):
    product_id: UUID
    timestamp: datetime.datetime = Field(default=datetime.datetime.now(datetime.UTC))
