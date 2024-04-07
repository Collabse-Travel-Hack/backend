import datetime
from typing import Type

from hatchet_sdk import Context

from src.workflows import redis_client
from src.workflows.config import settings
from src.workflows.fetcher.base import BaseFetcher
from src.workflows.fetcher.queries import build_query
from src.workflows.hatchet import hatchet
from src.workflows.loader.loader import BaseLoader


@hatchet.workflow(on_crons=["1 * * * *"])
class MongoEtlRag:
    def __init__(self, fetcher: BaseFetcher, loader: BaseLoader):
        self._fetcher = fetcher
        self._loader = loader

    @hatchet.step()
    def start_events_etl(self, context: Context):
        threshold = redis_client.client.get(settings.timestamp_name) or str(
            datetime.datetime.min
        )
        for documents in self._fetcher.fetch_many(query=build_query(date=threshold)):
            for document in documents:
                document["_id"] = document["id"]
            self._loader.load_batch(documents)
