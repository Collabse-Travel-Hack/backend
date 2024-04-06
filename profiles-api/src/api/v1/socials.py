from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException, Query
from src.schemas.result import GenericResult
from src.schemas.token import Token
from src.services.auth import AuthServiceABC
from src.services.social_providers import SocialNetworkProvider, get_provider
from src.services.user import UserServiceABC

router = APIRouter()


@router.post(
    "/login/{provider_name}",
    response_model=Token,
)
async def login_by_social_network(
    code: str = Query(None, description="Code from auth provider"),
    provider: SocialNetworkProvider = Depends(get_provider),
    user_service: UserServiceABC = Depends(),
    auth: AuthServiceABC = Depends(),
):
    user = await provider.process_user(code, user_service)

    token: GenericResult[Token] = await auth.login_by_oauth(
        login=user.response.login,
    )
    if not token.is_success:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail="login or/and password incorrect"
        )

    return token.response
