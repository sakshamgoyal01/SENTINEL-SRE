from sqlalchemy import select

from backend.models.auth.role_permission import (
    RolePermission
)

from backend.repositories.base_repository import (
    BaseRepository
)


class RolePermissionRepository(
    BaseRepository[
        RolePermission
    ]
):

    def __init__(
        self,
        session,
    ):
        super().__init__(
            session=session,
            model=RolePermission,
        )

    async def get_role_permissions(
        self,
        role_id: str,
    ) -> list[RolePermission]:

        statement = (
            select(
                RolePermission
            )
            .where(
                RolePermission.role_id
                == role_id
            )
        )

        result = await (
            self.session.execute(
                statement
            )
        )

        return list(
            result.scalars().all()
        )