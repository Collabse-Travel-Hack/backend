from uuid import UUID

from src.models.seen_media import MediaTypeEnum
from src.schemas.base import BaseEventSchema


class SeenMediaSchema(BaseEventSchema):
    media_type: MediaTypeEnum
    media_id: UUID
    media_name: str
