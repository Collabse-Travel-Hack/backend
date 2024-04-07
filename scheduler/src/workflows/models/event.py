from enum import StrEnum

from pydantic import Field, Extra

from src.workflows.models.base import BaseDataModel


class EventDataModel(BaseDataModel):
    duration: int
    is_can_buy: bool
    russpass_recommendation: bool
    event_type: str | None
    payment_method: str | None
    type_audio_guides: str | None
    city: str | None
    metro: str | None
    general_rating: float | None = Field(None)
    marks_count: int | None = Field(None)
    publication_date: str | None = Field(None)
    min_age: int | None = Field(None)
    ticket_price: float | None = Field(None)
    tags: list | None = Field(default_factory=list)
    sentiment: float | None = Field(None)
    flesch_reading_ease: float | None = Field(None)
    text_length: int | None = Field(None)

    class Config:
        str_strip_whitespace = True
        str_min_length = 0
        extra = Extra.allow
