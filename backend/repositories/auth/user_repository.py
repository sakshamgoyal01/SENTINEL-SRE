from sqlalchemy import select

from backend.models.auth.user import (
    User
)

from backend.repositories.base_repository import (
    BaseRepository
)


class UserRepository(
    BaseRepository[User]
):

    def __init__(
        self,
        session,
    ):
        super().__init__(
            session=session,
            model=User,
        )

    async def get_by_email(
        self,
        email: str,
    ) -> User | None:

        statement = (
            select(User)
            .where(
                User.email == email
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

    async def get_by_username(
        self,
        username: str,
    ) -> User | None:

        statement = (
            select(User)
            .where(
                User.username
                == username
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