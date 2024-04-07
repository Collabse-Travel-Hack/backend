from typing import Any

from elasticsearch import Elasticsearch, helpers

from src.workflows.config import settings
from src.workflows.loader.loader import BaseLoader


class ElasticLoader(BaseLoader):
    def __init__(self, es_client: Elasticsearch, index_name: str):
        self._es_client = es_client
        self._index_name = index_name

    async def load_batch(
        self, items: list[dict[str, Any]], batch_size: int = settings.batch_size
    ):
        for item in items:
            item["_index"] = self._index_name
        lines, _ = helpers.bulk(
            client=self._es_client,
            actions=items,
            index=self._index_name,
            chunk_size=batch_size,
        )
        return lines
