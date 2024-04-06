from src.models.clicked import ContentTypeEnum
from src.schemas.base import BaseEventSchema


class ClickedEventSchema(BaseEventSchema):
    type: ContentTypeEnum
