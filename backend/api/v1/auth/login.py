from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from backend.api.dependencies.auth import (
    get_auth_service,
)

from backend.schemas.auth.login import (
    LoginRequest,
)

from backend.schemas.auth.token import (
    TokenResponse,
)

from backend.auth.jwt import (
    create_access_token,
)

from backend.auth.password import (
    verify_password,
)

router = APIRouter()


@router.post(
    "/login",
    response_model=TokenResponse,
)
async def login(
    request: LoginRequest,
    auth_service=Depends(
        get_auth_service
    ),
):
    user = await (
        auth_service.authenticate(
            email=request.email,
            password=request.password,
            verify_password=verify_password,
        )
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    session = (
        auth_service
        .user_repository
        .session
    )

    from backend.repositories.auth.user_role_repository import (
        UserRoleRepository,
    )

    from backend.repositories.auth.role_repository import (
        RoleRepository,
    )

    user_role_repo = (
        UserRoleRepository(
            session
        )
    )

    role_repo = (
        RoleRepository(
            session
        )
    )

    mappings = await (
        user_role_repo
        .get_user_roles(
            str(user.id)
        )
    )

    roles: list[str] = []

    for mapping in mappings:

        role = await (
            role_repo.get_by_id(
                mapping.role_id
            )
        )

        if role:
            roles.append(
                role.name
            )

    # Prevent accidental lockout
    if (
        user.is_superuser
        and "ADMIN" not in roles
    ):
        roles.append(
            "ADMIN"
        )

    token = create_access_token(
        subject=str(user.id),
        email=user.email,
        roles=roles,
    )

    return TokenResponse(
        access_token=token,
        expires_in=3600,
    )