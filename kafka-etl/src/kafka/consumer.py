from aiokafka import AIOKafkaConsumer

from src.core.config import settings


class KafkaConsumer:
    def __init__(self):
        self.consumer = AIOKafkaConsumer(
            settings.kafka_seen_media_topic,
            settings.kafka_click_topic,
            settings.kafka_bookmark_topic,
            settings.kafka_buy_topic,
            settings.kafka_commented_topic,
            settings.kafka_uploaded_topic,
            bootstrap_servers=f"{settings.KAFKA_HOST}:{settings.KAFKA_PORT}",
            group_id=settings.KAFKA_GROUP,
        )

    async def consume_messages(self):
        await self.consumer.start()
        try:
            while True:
                result = await self.consumer.getmany(timeout_ms=1000, max_records=1000)
                for tp, messages in result.items():
                    yield messages
        finally:
            await self.consumer.stop()
