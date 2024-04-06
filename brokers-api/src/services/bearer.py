from http import HTTPStatus

import backoff
from aiohttp import ClientSession
from circuitbreaker import CircuitBreakerError, circuit
from fastapi import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.core.config import BACKOFF_CONFIG, CIRCUIT_CONFIG, settings
from src.exceptions.bad_request import BadRequest
from src.exceptions.rate import RateLimitException
from src.schemas.account import Account
from src.schemas.token_payload import TokenPayload


@backoff.on_exception(**BACKOFF_CONFIG)
@circuit(**CIRCUIT_CONFIG)
async def get_account_info(token: str) -> Account:
    token_payload = TokenPayload(access_token=token).model_dump(mode="json")
    async with ClientSession() as session:
        response = await session.post(
            url=settings.profile_path,
            json=token_payload,
            headers={"Content-Type": "application/json"},
        )
        if response.status == HTTPStatus.TOO_MANY_REQUESTS:
            raise RateLimitException()
        if response.status != HTTPStatus.OK:
            raise BadRequest(message=response.reason, status_code=response.status)
        body = await response.json()
        return Account(**body)


class JwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        try:
            credentials: HTTPAuthorizationCredentials = await super().__call__(request)
            if not credentials:
                raise BadRequest(
                    status_code=HTTPStatus.FORBIDDEN,
                    message="Invalid authorization code",
                )
            if not credentials.scheme == "Bearer":
                raise BadRequest(
                    status_code=HTTPStatus.UNAUTHORIZED,
                    message="Only Bearer token might be accepted",
                )
            return await self.get_account(token=credentials.credentials)

        except CircuitBreakerError:
            raise BadRequest(
                status_code=HTTPStatus.UNAUTHORIZED, message="Service unavailable"
            )

    @staticmethod
    async def get_account(token: str) -> Account:
        return await get_account_info(token=token)


security_jwt = JwtBearer()
