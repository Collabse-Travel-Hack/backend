from aiokafka import AIOKafkaProducer
from src.models.base import BaseEvent
from src.schemas.account import Account
from src.services.base import MessageProducerABC, MessageServiceABC


class KafkaMessageProducer(MessageProducerABC):
    def __init__(self, broker: AIOKafkaProducer):
        self._broker = broker

    async def publish(self, topic: str, message: str, key: str) -> None:
        await self._broker.send(
            topic=topic, value=message.encode("utf-8"), key=key.encode("utf-8")
        )


class MessageService(MessageServiceABC):
    def __init__(self, broker: MessageProducerABC):
        self._broker = broker

    async def send_message(
        self, topic: str, message: BaseEvent, account: Account | None = None
    ) -> None:
        await self._broker.publish(
            topic=topic,
            message=message.model_dump_json(),
            key=message.account_id.hex if message.account_id else "anonymus",
        )
