from functools import cache

from aiokafka import AIOKafkaProducer
from fastapi import Depends
from src.broker.kafka import get_producer
from src.dependencies.registrator import add_factory_to_mapper
from src.services.base import MessageProducerABC, MessageServiceABC
from src.services.messages import KafkaMessageProducer, MessageService


@add_factory_to_mapper(MessageProducerABC)
@cache
def create_message_producer(
    broker: AIOKafkaProducer = Depends(get_producer),
) -> KafkaMessageProducer:
    return KafkaMessageProducer(broker=broker)


@add_factory_to_mapper(MessageServiceABC)
@cache
def create_message_service(producer: MessageProducerABC = Depends()) -> MessageService:
    return MessageService(broker=producer)
