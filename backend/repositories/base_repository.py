from typing import Generic
from typing import TypeVar

from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import delete

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from backend.repositories.filters import (
    FilterParams
)
from backend.repositories.pagination import (
    PaginationParams
)
from backend.repositories.sorting import (
    SortParams
)


ModelType = TypeVar("ModelType")


class BaseRepository(
    Generic[ModelType]
):

    def __init__(
        self,
        session: AsyncSession,
        model: type[ModelType]
    ):
        self.session = session
        self.model = model

    async def create(
        self,
        entity: ModelType
    ) -> ModelType:

        self.session.add(entity)

        await self.session.flush()

        await self.session.refresh(entity)

        return entity

    async def get_by_id(
        self,
        entity_id,
    ) -> ModelType | None:

        statement = (
            select(self.model)
            .where(
                self.model.id == entity_id
            )
        )

        result = await self.session.execute(
            statement
        )

        return result.scalar_one_or_none()

    async def list(
            self,
            pagination: PaginationParams | None = None,
    ) -> list[ModelType]:
        statement = select(self.model)

        if pagination is not None:
            statement = (
                statement
                .offset(
                    pagination.offset
                )
                .limit(
                    pagination.limit
                )
            )

        result = await self.session.execute(
            statement
        )

        return list(
            result.scalars().all()
        )

    async def update(
        self,
        entity: ModelType
    ) -> ModelType:

        await self.session.flush()

        await self.session.refresh(entity)

        return entity

    async def delete(
        self,
        entity_id,
    ) -> None:

        statement = (
            delete(self.model)
            .where(
                self.model.id == entity_id
            )
        )

        await self.session.execute(
            statement
        )

    async def count(self) -> int:

        statement = (
            select(
                func.count()
            ).select_from(
                self.model
            )
        )

        result = await self.session.execute(
            statement
        )

        return int(
            result.scalar_one()
        )

    async def exists(
        self,
        entity_id
    ) -> bool:

        return (
            await self.get_by_id(
                entity_id
            )
        ) is not None