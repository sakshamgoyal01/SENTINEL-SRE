from backend.models.auth.user import (
    User
)

from backend.services.base_service import (
    BaseService
)


class UserService(
    BaseService
):

    async def create_user(
        self,
        email: str,
        username: str,
        password_hash: str,
        is_superuser: bool = False,
    ) -> User:

        user = User(
            email=email,
            username=username,
            password_hash=password_hash,
            is_active=True,
            is_superuser=is_superuser,
        )

        return await (
            self.repository.create(
                user
            )
        )

    async def disable_user(
        self,
        user: User,
    ) -> User:

        user.is_active = False

        return await (
            self.repository.update(
                user
            )
        )

    async def enable_user(
        self,
        user: User,
    ) -> User:

        user.is_active = True

        return await (
            self.repository.update(
                user
            )
        )

    async def change_password(
        self,
        user: User,
        password_hash: str,
    ) -> User:

        user.password_hash = (
            password_hash
        )

        return await (
            self.repository.update(
                user
            )
        )