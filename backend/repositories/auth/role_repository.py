from sqlalchemy import select

from backend.models.auth.role import (
    Role
)

from backend.repositories.base_repository import (
    BaseRepository
)


class RoleRepository(
    BaseRepository[Role]
):

    def __init__(
        self,
        session,
    ):
        super().__init__(
            session=session,
            model=Role,
        )

    async def get_by_name(
        self,
        name: str,
    ) -> Role | None:

        statement = (
            select(Role)
            .where(
                Role.name == name
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