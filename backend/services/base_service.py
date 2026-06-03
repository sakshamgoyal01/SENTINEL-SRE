from backend.repositories.pagination import (
    PaginationParams
)


class BaseService:

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    async def create(
        self,
        entity,
    ):
        return await (
            self.repository.create(
                entity
            )
        )

    async def get(
        self,
        entity_id,
    ):
        return await (
            self.repository.get_by_id(
                entity_id
            )
        )

    async def list(
        self,
        pagination: PaginationParams,
    ):
        return await (
            self.repository.list(
                pagination
            )
        )

    async def update(
        self,
        entity,
    ):
        return await (
            self.repository.update(
                entity
            )
        )

    async def delete(
        self,
        entity_id,
    ):
        return await (
            self.repository.delete(
                entity_id
            )
        )

    async def exists(
        self,
        entity_id,
    ):
        return await (
            self.repository.exists(
                entity_id
            )
        )

    async def count(
        self,
    ):
        return await (
            self.repository.count()
        )