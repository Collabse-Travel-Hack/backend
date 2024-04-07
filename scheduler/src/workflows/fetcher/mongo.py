from typing import Self

from pydantic import MongoDsn
from pymongo import MongoClient

from src.workflows.config import settings
from src.workflows.fetcher.base import BaseFetcher


class MongoFetcher(BaseFetcher):
    def __init__(
        self,
        mongo_client: MongoClient,
        database_name: str = settings.mongo_database,
        collection_name: str = settings.mongo_collection,
    ) -> None:
        self.mongo_client = mongo_client
        self.database_name = database_name
        self.collection_name = collection_name
        self._collection = self.mongo_client[self.database_name][self.collection_name]

    def fetch_many(
        self, query: dict = None, size: int = settings.batch_size, *args, **kwargs
    ):
        filter_dict = query or {}
        for documents in self._collection.find(filter_dict, batch_size=size):
            yield documents
