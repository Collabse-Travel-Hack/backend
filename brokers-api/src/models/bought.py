from src.models.base import BaseEvent


class BoughtEvent(BaseEvent):
    price: float | None = None
