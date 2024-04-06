import datetime
from dataclasses import dataclass
from uuid import UUID

from src.schemas.events import ContentTypeEnum
from src.schemas.media_type import MediaTypeEnum


@dataclass
class KafkaEvent:
    timestamp: datetime.datetime
    account_id: UUID
    product_id: UUID
    user_agent: str


@dataclass
class KafkaBookmarkedEvent(KafkaEvent):
    ...


@dataclass
class KafkaBoughtEvent(KafkaEvent):
    price: float | None = None


@dataclass
class KafkaClickedEvent(KafkaEvent):
    type: ContentTypeEnum


@dataclass
class KafkaCommentedEvent(KafkaEvent):
    text: str


@dataclass
class KafkaMediaUploadedEvent(KafkaEvent):
    media_type: MediaTypeEnum
    media_id: UUID
    media_name: str


@dataclass
class KafkaSeenMediaEvent(KafkaMediaUploadedEvent):
    ...
