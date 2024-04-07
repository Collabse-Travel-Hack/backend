from src.workflows.models.event import EventDataModel


def build_query(date: str) -> dict:
    return {"publication_date": {"gt": date}}


MAPPINGS = {type(EventDataModel): {}}
