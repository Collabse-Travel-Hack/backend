from enum import IntEnum

from src.models.base import BaseEvent


class ContentTypeEnum(IntEnum):
    voucher = 0
    product = 1
    description = 2
    bought = 3


class ClickedEvent(BaseEvent):
    type: ContentTypeEnum
