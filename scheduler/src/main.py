import asyncio
import logging

from elasticsearch import Elasticsearch
from pymongo import MongoClient
from redis.asyncio import Redis

from src.workflows import redis_client, elastic
from src.workflows.config import settings
from src.workflows.fetcher.mongo import MongoFetcher
from src.workflows.hatchet import hatchet
from src.workflows.loader.elastic import ElasticLoader
from src.workflows import mongo_client
from src.workflows.mongo_etl_rag import MongoEtlRag


def build_fetcher(mongo_client: MongoClient, database_name: str, collection_name: str):
    return MongoFetcher(mongo_client, database_name, collection_name)


def build_elastic_fetcher(elastic_client: Elasticsearch, index_name: str):
    return ElasticLoader(es_client=elastic_client, index_name=index_name)


async def main():
    try:
        redis_client.client = Redis(host=settings.cache_host, port=settings.cache_port)
        elastic.elastic_client = Elasticsearch(hosts=[settings.elastic_host])
        mongo_client.mongo_client = MongoClient(host=settings.mongo_database)
        worker = hatchet.worker("etl-worker")
        fetcher = MongoFetcher(
            mongo_client=mongo_client.mongo_client,
            database_name=settings.mongo_database,
            collection_name=settings.mongo_collection,
        )
        loader = ElasticLoader(
            es_client=elastic.elastic_client, index_name=settings.elastic_collection
        )

        worker.register_workflow(MongoEtlRag(fetcher=fetcher, loader=loader))
        worker.start()
    except Exception as e:
        logging.error(e)
    finally:
        if redis_client.client:
            await redis_client.client.aclose()
        if elastic.elastic_client:
            elastic.elastic_client.close()


if __name__ == "__main__":
    asyncio.run(main())
