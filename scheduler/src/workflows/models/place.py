import datetime
from enum import StrEnum

from pydantic import Field

from src.workflows.models.base import BaseDataModel


class ObjectTypeEnum(StrEnum):
    PLACE = "PLACE"
    EVENT = "EVENT"
    RESTAURANT = "RESTAURANT"
    TRACK = "TRACK"
    EXCURSION = "EXCURSION"


class PlaceDataModel(BaseDataModel):
    address: str | None = Field(None)
    metro_station: str | None = Field(None)
    object_type: ObjectTypeEnum
    popularity: float
    title: str
    description: str | None = Field(None)
    has_audio_guide: bool | None = Field(None)
    is_can_buy: bool | None = Field(None)
    price: float | None = Field(None)
    russpass_recommendation: bool | None = Field(None)
    rating: float | None = Field(None)
    type: str | None = Field(None)

    class Config:
        str_strip_whitespace = True
        str_min_length = 0
        extra = Extra.allow
