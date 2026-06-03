from sqlalchemy import select

from backend.models.auth.permission import (
    Permission
)

from backend.repositories.base_repository import (
    BaseRepository
)


class PermissionRepository(
    BaseRepository[
        Permission
    ]
):

    def __init__(
        self,
        session,
    ):
        super().__init__(
            session=session,
            model=Permission,
        )

    async def get_by_name(
        self,
        name: str,
    ) -> Permission | None:

        statement = (
            select(Permission)
            .where(
                Permission.name
                == name
            )
        )

        result = await (
            self.session.execute(
                statement
            )
        )

        return (
            result.scalar_one_or_none()
        )