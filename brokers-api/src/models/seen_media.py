from enum import IntEnum
from uuid import UUID

from src.models.base import BaseEvent


class MediaTypeEnum(IntEnum):
    image = 0
    video = 1
    audio = 2


class SeenMediaEvent(BaseEvent):
    media_type: MediaTypeEnum
    media_id: UUID
    media_name: str
