import logging

from src.models.events import (
    KafkaBookmarkedEvent,
    KafkaBoughtEvent,
    KafkaClickedEvent,
    KafkaCommentedEvent,
    KafkaMediaUploadedEvent,
    KafkaSeenMediaEvent,
)
from src.schemas.events import ContentTypeEnum


def process_clicked_event(message, timestamp):
    try:
        message["type"] = ContentTypeEnum(message["type"])
        logging.info(message)
        event = KafkaClickedEvent(**message)
        return {
            "timestamp": timestamp,
            "type": event.type.name,
            "account_id": event.account_id or "anonymus",
            "product_id": event.product_id,
            "user_agent": event.user_agent,
        }
    except Exception as e:
        logging.error(e)


def process_bookmarked_event(message, timestamp):
    try:
        event = KafkaBookmarkedEvent(**message)
        return {
            "timestamp": timestamp,
            "account_id": event.account_id or "anonymus",
            "product_id": event.product_id,
            "user_agent": event.user_agent,
        }
    except Exception as e:
        logging.error(e)


def process_bought_event(message, timestamp):
    try:
        event = KafkaBoughtEvent(**message)
        return {
            "timestamp": timestamp,
            "account_id": event.account_id or "anonymus",
            "product_id": event.product_id,
            "price": event.price,
            "user_agent": event.user_agent,
        }
    except Exception as e:
        logging.error(e)


def process_commented_event(message, timestamp):
    try:
        event = KafkaCommentedEvent(**message)
        return {
            "timestamp": timestamp,
            "account_id": event.account_id or "anonymus",
            "product_id": event.product_id,
            "text": event.text,
            "user_agent": event.user_agent,
        }
    except Exception as e:
        logging.error(e)


def process_media_uploaded_event(message, timestamp):
    try:
        event = KafkaMediaUploadedEvent(**message)
        return {
            "timestamp": timestamp,
            "account_id": event.account_id or "anonymus",
            "product_id": event.product_id,
            "media_type": event.media_type,
            "media_id": event.media_id,
            "media_name": event.media_name,
            "user_agent": event.user_agent,
        }
    except Exception as e:
        logging.error(e)


def process_seen_event(message, timestamp):
    try:
        event = KafkaSeenMediaEvent(**message)
        return {
            "timestamp": timestamp,
            "account_id": event.account_id or "anonymus",
            "product_id": event.product_id,
            "media_type": event.media_type,
            "media_id": event.media_id,
            "media_name": event.media_name,
            "user_agent": event.user_agent,
        }
    except Exception as e:
        logging.error(e)
