from src.schemas.base import BaseEventSchema


class BoughtSchema(BaseEventSchema):
    price: float | None = None
