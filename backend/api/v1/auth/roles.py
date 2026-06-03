from fastapi import APIRouter
from fastapi import Depends

from pydantic import BaseModel

from backend.api.dependencies.auth import (
    get_role_service,
)

router = APIRouter()


class AssignRoleRequest(
    BaseModel
):
    user_id: str
    role_id: str


@router.get("/")
async def list_roles(
    role_service=Depends(
        get_role_service
    ),
):
    return await (
        role_service.list_roles()
    )


@router.post(
    "/assign"
)
async def assign_role(
    request: AssignRoleRequest,
    role_service=Depends(
        get_role_service
    ),
):
    mapping = await (
        role_service.assign_role(
            request.user_id,
            request.role_id,
        )
    )

    await (
        role_service
        .user_role_repository
        .session
        .commit()
    )

    return mapping