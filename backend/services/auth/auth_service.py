from datetime import datetime
from datetime import UTC

from backend.models.auth.user import (
    User
)


class AuthService:

    def __init__(
        self,
        user_repository,
    ):
        self.user_repository = (
            user_repository
        )

    async def authenticate(
        self,
        email: str,
        password: str,
        verify_password,
    ) -> User | None:

        user = await (
            self.user_repository
            .get_by_email(
                email
            )
        )

        if user is None:
            return None

        if not verify_password(
            password,
            user.password_hash,
        ):
            return None

        user.last_login = (
            datetime.now(
                UTC
            )
        )

        await (
            self.user_repository
            .update(
                user
            )
        )

        return user

    async def get_user_by_email(
        self,
        email: str,
    ) -> User | None:

        return await (
            self.user_repository
            .get_by_email(
                email
            )
        )

    async def get_user_by_username(
        self,
        username: str,
    ) -> User | None:

        return await (
            self.user_repository
            .get_by_username(
                username
            )
        )