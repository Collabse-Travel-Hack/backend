from src.workflows.hatchet import hatchet
from src.workflows.mongo_etl_rag import MongoEtlRag

worker = hatchet.worker('first-worker')
worker.register_workflow(MongoEtlRag())

worker.start()