import asyncio
import logging

from clickhouse_driver import Client

from src.core.config import settings


class ClickHouseClient:
    def __init__(self):
        self.client = Client(host=settings.CH_HOST, port=settings.CH_PORT)
        self.buffers = {
            "kafka_seen_media_events": [],
            "kafka_clicked_events": [],
            "kafka_bookmarked_events": [],
            "kafka_bought_events": [],
            "kafka_commented_events": [],
            "kafka_media_uploaded_events": [],
        }
        self.buffer_limit = 1000  # Максимальный размер буфера для каждого типа события
        self.loop = asyncio.get_event_loop()
        self.loop.create_task(self.flush_buffers_periodically())

        # Маппинг типов событий на соответствующие запросы
        self.query_mapping = {
            "kafka_seen_media_events": "INSERT INTO kafka_seen_media_events (timestamp, account_id, product_id, media_type, media_id, media_name, author_id, event_type) VALUES",
            "kafka_clicked_events": "INSERT INTO kafka_clicked_events (timestamp, account_id, product_id, type, author_id, event_type) VALUES",
            "kafka_bookmarked_events": "INSERT INTO kafka_bookmarked_events (timestamp, account_id, product_id, author_id, event_type) VALUES",
            "kafka_bought_events": "INSERT INTO kafka_bought_events (timestamp, account_id, product_id, price, author_id, event_type) VALUES",
            "kafka_commented_events": "INSERT INTO kafka_commented_events (timestamp, account_id, product_id, text, author_id, event_type) VALUES",
            "kafka_media_uploaded_events": "INSERT INTO kafka_media_uploaded_events (timestamp, account_id, product_id, media_type, media_id, media_name, author_id, event_type) VALUES",
        }

    async def flush_buffers_periodically(self):
        while True:
            await asyncio.sleep(60)  # Периодическая отправка каждые 60 секунд
            for event_type in self.buffers.keys():
                if self.buffers[event_type]:
                    await self.flush_buffer(event_type)

    async def flush_buffer(self, event_type):
        try:
            data_batch = self.buffers[event_type]
            if not data_batch:
                return

            query = self.query_mapping[event_type]
            self.client.execute(query, data_batch)

            self.buffers[event_type] = []  # Очищаем буфер после отправки
        except Exception as e:
            logging.error(e)

    def add_event(self, event_type, data):
        try:
            self.buffers[event_type].append(data)
            if len(self.buffers[event_type]) >= self.buffer_limit:
                asyncio.create_task(
                    self.flush_buffer(event_type)
                )  # Асинхронная отправка при достижении лимита буфера
        except Exception as e:
            logging.info(e)
