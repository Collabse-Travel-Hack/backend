import json
import logging
from datetime import datetime

from aiokafka import ConsumerRecord

from src.core.config import settings
from src.data_processor import (
    process_clicked_event,
    process_seen_event,
    process_bought_event,
    process_commented_event,
    process_bookmarked_event,
    process_media_uploaded_event,
)

logger = logging.getLogger(__name__)


class MessageRouter:
    def __init__(self, clickhouse_client):
        self.clickhouse_client = clickhouse_client
        self.topic_to_process_and_event_type = {
            settings.kafka_seen_media_topic: (
                process_seen_event,
                "kafka_seen_media_events",
            ),
            settings.kafka_click_topic: (
                process_clicked_event,
                "kafka_clicked_events",
            ),
            settings.kafka_bookmark_topic: (
                process_bookmarked_event,
                "kafka_bookmarked_events",
            ),
            settings.kafka_buy_topic: (
                process_bought_event,
                "kafka_bought_events",
            ),
            settings.kafka_commented_topic: (
                process_commented_event,
                "kafka_commented_events",
            ),
            settings.kafka_uploaded_topic: (
                process_media_uploaded_event,
                "kafka_uploaded_events",
            ),
        }

    async def route_message(self, msg: ConsumerRecord):
        try:
            topic_name = msg.topic
            if topic_name in self.topic_to_process_and_event_type:
                process_function, event_type = self.topic_to_process_and_event_type[
                    topic_name
                ]
                timestamp = datetime.fromtimestamp(msg.timestamp / 1000.0)
                message = json.loads(msg.value.decode("utf-8"))
                data = process_function(message, timestamp)
                logging.info(f"Processed event data {data}, {event_type}")
                self.clickhouse_client.add_event(event_type, data)
            else:
                logger.warning(f"Нет обработчика для топика {topic_name}")
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка декодирования JSON: {e}")
