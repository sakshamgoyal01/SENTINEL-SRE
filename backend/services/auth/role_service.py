from backend.models.auth.user_role import (
    UserRole
)

from backend.services.base_service import (
    BaseService
)


class RoleService:

    def __init__(
        self,
        role_repository,
        user_role_repository,
    ):
        self.role_repository = (
            role_repository
        )

        self.user_role_repository = (
            user_role_repository
        )

    async def assign_role(
        self,
        user_id: str,
        role_id: str,
    ) -> UserRole:

        mapping = UserRole(
            user_id=user_id,
            role_id=role_id,
        )

        return await (
            self.user_role_repository
            .create(
                mapping
            )
        )

    async def remove_role(
        self,
        mapping: UserRole,
    ) -> None:

        await (
            self.user_role_repository
            .delete(
                mapping.id
            )
        )

    async def list_roles(
            self,
    ):
        return await (
            self.role_repository
            .list()
        )

    async def get_user_roles(
            self,
            user_id: str,
    ):
        return await (
            self.user_role_repository
            .get_user_roles(
                user_id
            )
        )