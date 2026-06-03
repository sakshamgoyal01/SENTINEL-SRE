from sqlalchemy import select

from backend.models.auth.user_role import (
    UserRole
)

from backend.repositories.base_repository import (
    BaseRepository
)


class UserRoleRepository(
    BaseRepository[
        UserRole
    ]
):

    def __init__(
        self,
        session,
    ):
        super().__init__(
            session=session,
            model=UserRole,
        )

    async def get_user_roles(
        self,
        user_id: str,
    ) -> list[UserRole]:

        statement = (
            select(UserRole)
            .where(
                UserRole.user_id
                == user_id
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