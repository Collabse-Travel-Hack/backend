from uuid import UUID

from src.models.base import BaseEvent
from src.models.seen_media import MediaTypeEnum


class MediaUploadedEvent(BaseEvent):
    media_type: MediaTypeEnum
    media_id: UUID
    media_name: str
