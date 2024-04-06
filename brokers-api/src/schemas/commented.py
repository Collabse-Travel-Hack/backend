from src.schemas.base import BaseEventSchema


class CommentedEventSchema(BaseEventSchema):
    text: str
