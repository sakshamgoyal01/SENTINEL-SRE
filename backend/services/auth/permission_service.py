from backend.models.auth.role_permission import (
    RolePermission
)


class PermissionService:

    def __init__(
        self,
        permission_repository,
        role_permission_repository,
    ):
        self.permission_repository = (
            permission_repository
        )

        self.role_permission_repository = (
            role_permission_repository
        )

    async def assign_permission(
        self,
        role_id: str,
        permission_id: str,
    ) -> RolePermission:

        mapping = RolePermission(
            role_id=role_id,
            permission_id=permission_id,
        )

        return await (
            self.role_permission_repository
            .create(
                mapping
            )
        )

    async def remove_permission(
        self,
        mapping: RolePermission,
    ) -> None:

        await (
            self.role_permission_repository
            .delete(
                mapping.id
            )
        )