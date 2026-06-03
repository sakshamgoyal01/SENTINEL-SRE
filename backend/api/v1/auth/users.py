from fastapi import APIRouter
from fastapi import Depends

from backend.api.dependencies.auth import (
    get_user_service,
)

from backend.auth.password import (
    hash_password,
)

from backend.schemas.auth.user import (
    CreateUserRequest,
    UserResponse,
)

router = APIRouter()


@router.get(
    "/",
    response_model=list[UserResponse],
)
async def list_users(
    user_service=Depends(
        get_user_service
    ),
):
    return await (
        user_service.list(
            pagination=None
        )
    )


@router.post(
    "/",
    response_model=UserResponse,
)
async def create_user(
    request: CreateUserRequest,
    user_service=Depends(
        get_user_service
    ),
):
    password_hash = hash_password(
        request.password
    )

    user = await (
        user_service.create_user(
            email=request.email,
            username=request.username,
            password_hash=password_hash,
        )
    )

    await (
        user_service.repository.session.commit()
    )

    return user