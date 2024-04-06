from src.models.base import BaseEvent


class CommentedEvent(BaseEvent):
    text: str
