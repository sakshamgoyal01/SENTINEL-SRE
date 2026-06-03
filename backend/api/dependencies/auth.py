from fastapi import Depends

from backend.database.session import (
    get_db,
)

from backend.core.container import (
    Container,
)


async def get_auth_service(
    session=Depends(get_db),
):
    container = Container(
        session
    )

    return (
        container.auth_service
    )


async def get_user_service(
    session=Depends(get_db),
):
    container = Container(
        session
    )

    return (
        container.user_service
    )


async def get_role_service(
    session=Depends(get_db),
):
    container = Container(
        session
    )

    return (
        container.role_service
    )