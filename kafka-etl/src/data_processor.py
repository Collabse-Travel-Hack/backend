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
            "type": event.type,
            "account_id": event.account_id,
            "product_id": event.product_id,
            "author_id": event.author_id,
            "event_type": event.event_type,
        }
    except Exception as e:
        print(e)


def process_bookmarked_event(message, timestamp):
    event = KafkaBookmarkedEvent(**message)
    return {
        "timestamp": timestamp,
        "account_id": event.account_id,
        "product_id": event.product_id,
        "author_id": event.author_id,
        "event_type": event.event_type,
    }


def process_bought_event(message, timestamp):
    event = KafkaBoughtEvent(**message)
    return {
        "timestamp": timestamp,
        "account_id": event.account_id,
        "product_id": event.product_id,
        "price": event.price,
        "author_id": event.author_id,
        "event_type": event.event_type,
    }


def process_commented_event(message, timestamp):
    event = KafkaCommentedEvent(**message)
    return {
        "timestamp": timestamp,
        "account_id": event.account_id,
        "product_id": event.product_id,
        "text": event.text,
        "author_id": event.author_id,
        "event_type": event.event_type,
    }


def process_media_uploaded_event(message, timestamp):
    event = KafkaMediaUploadedEvent(**message)
    return {
        "timestamp": timestamp,
        "account_id": event.account_id,
        "product_id": event.product_id,
        "media_type": event.media_type,
        "media_id": event.media_id,
        "media_name": event.media_name,
        "author_id": event.author_id,
        "event_type": event.event_type,
    }


def process_seen_event(message, timestamp):
    event = KafkaSeenMediaEvent(**message)
    return {
        "timestamp": timestamp,
        "account_id": event.account_id,
        "product_id": event.product_id,
        "media_type": event.media_type,
        "media_id": event.media_id,
        "media_name": event.media_name,
        "author_id": event.author_id,
        "event_type": event.event_type,
    }
