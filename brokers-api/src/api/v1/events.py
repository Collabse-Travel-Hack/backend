from typing import Annotated

from fastapi import APIRouter, Depends, Header
from src.core.config import settings
from src.models.bookmarked import BookmarkedEvent
from src.models.bought import BoughtEvent
from src.models.clicked import ClickedEvent
from src.models.commented import CommentedEvent
from src.models.media_uploaded import MediaUploadedEvent
from src.models.seen_media import SeenMediaEvent
from src.schemas.account import Account
from src.schemas.bookmarked import BookmarkEventSchema
from src.schemas.bought import BoughtSchema
from src.schemas.clicked import ClickedEventSchema
from src.schemas.commented import CommentedEventSchema
from src.schemas.media_uploaded import MediaUploadedSchema
from src.schemas.seen_media import SeenMediaSchema
from src.services.base import MessageServiceABC
from src.services.bearer import security_jwt

router = APIRouter()


@router.post(
    "/bookmarked",
    summary="Отправить событие о помещении сведений об услуге в закладки",
    description="Отправка события в брокер сообщений",
    tags=["События"],
)
async def send_bookmarked_event(
    bookmarked_event: BookmarkEventSchema,
    message_service: MessageServiceABC = Depends(),
    account: Annotated[Account, Depends(security_jwt)] = None,
    user_agent: Annotated[str | None, Header()] = None,
) -> None:
    await message_service.send_message(
        topic=settings.kafka_bookmark_topic,
        message=BookmarkedEvent(
            **bookmarked_event.model_dump(),
            account_id=account.id if account else None,
            user_agent=user_agent
        ),
        account=account,
    )


@router.post(
    "/clicked",
    summary="Отправить событие о клике в брокер сообщений",
    description="Отправка события в брокер сообщений",
    tags=["События"],
)
async def send_clicked(
    clicked_event: ClickedEventSchema,
    message_service: MessageServiceABC = Depends(),
    account: Annotated[Account, Depends(security_jwt)] = None,
    user_agent: Annotated[str | None, Header()] = None,
) -> None:
    await message_service.send_message(
        topic=settings.kafka_click_topic,
        message=ClickedEvent(
            **clicked_event.model_dump(),
            account_id=account.id if account else None,
            user_agent=user_agent
        ),
        account=account,
    )


@router.post(
    "/commented",
    summary="Отправить событие о комментировании в брокер сообщении",
    description="Отправка события в брокер сообщений",
    tags=["События"],
)
async def send_commented(
    commented_event: CommentedEventSchema,
    message_service: MessageServiceABC = Depends(),
    account: Annotated[Account, Depends(security_jwt)] = None,
    user_agent: Annotated[str | None, Header()] = None,
) -> None:
    await message_service.send_message(
        topic=settings.kafka_commented_topic,
        message=CommentedEvent(
            **commented_event.model_dump(),
            account_id=account.id if account else None,
            user_agent=user_agent
        ),
        account=account,
    )


@router.post(
    "/media-uploaded",
    summary="Отправка события в брокер сообщений",
    description="Отправить событие о прикреплении файлов к продукту",
    tags=["События"],
)
async def send_media_uploaded(
    media_uploaded_event: MediaUploadedSchema,
    message_service: MessageServiceABC = Depends(),
    account: Annotated[Account, Depends(security_jwt)] = None,
    user_agent: Annotated[str | None, Header()] = None,
) -> None:
    await message_service.send_message(
        topic=settings.kafka_media_uploaded_topic,
        message=MediaUploadedEvent(
            **media_uploaded_event.model_dump(),
            account_id=account.id if account else None,
            user_agent=user_agent
        ),
        account=account,
    )


@router.post(
    "/seen-media",
    summary="Отправка события в брокер сообщений",
    description="Отправить событие о просмотре",
    tags=["События"],
)
async def send_seen_media(
    seen_media_event: SeenMediaSchema,
    message_service: MessageServiceABC = Depends(),
    account: Annotated[Account, Depends(security_jwt)] = None,
    user_agent: Annotated[str | None, Header()] = None,
) -> None:
    await message_service.send_message(
        topic=settings.kafka_seen_media_topic,
        message=SeenMediaEvent(
            **seen_media_event.model_dump(),
            account_id=account.id if account else None,
            user_agent=user_agent
        ),
        account=account,
    )


@router.post(
    "/bought",
    description="Отправка события в брокер сообщений",
    summary="Отправить событие о покупке услуги",
    tags=["События"],
)
async def send_bought(
    bought_event: BoughtSchema,
    message_service: MessageServiceABC = Depends(),
    account: Annotated[Account, Depends(security_jwt)] = None,
    user_agent: Annotated[str | None, Header()] = None,
) -> None:
    await message_service.send_message(
        topic=settings.kafka_buy_topic,
        message=BoughtEvent(
            **bought_event.model_dump(),
            account_id=account.id if account else None,
            user_agent=user_agent
        ),
        account=account,
    )
