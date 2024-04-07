import datetime
import uuid
from dataclasses import dataclass
from uuid import UUID

from src.schemas.events import ContentTypeEnum
from src.schemas.media_type import MediaTypeEnum


@dataclass
class KafkaEvent:
    account_id: UUID
    product_id: UUID
    user_agent: UUID
    author_id: UUID | None = None
    event_type: str | None = None
    timestamp: datetime.datetime | None = None


@dataclass
class KafkaBookmarkedEvent(KafkaEvent):
    ...


@dataclass
class KafkaBoughtEvent(KafkaEvent):
    price: float | None = None


@dataclass
class KafkaClickedEvent(KafkaEvent):
    type: ContentTypeEnum = ContentTypeEnum.description


@dataclass
class KafkaCommentedEvent(KafkaEvent):
    text: str = ""


@dataclass
class KafkaMediaUploadedEvent(KafkaEvent):
    media_type: MediaTypeEnum = MediaTypeEnum.image
    media_id: UUID = uuid.uuid4()
    media_name: str = ""


@dataclass
class KafkaSeenMediaEvent(KafkaMediaUploadedEvent):
    ...
