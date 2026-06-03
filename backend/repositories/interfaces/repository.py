from typing import Protocol
from typing import Generic
from typing import TypeVar
from uuid import UUID

from backend.repositories.filters import (
    FilterParams
)
from backend.repositories.pagination import (
    PaginationParams
)
from backend.repositories.sorting import (
    SortParams
)


T = TypeVar("T")


class Repository(
    Protocol,
    Generic[T]
):

    async def create(
        self,
        entity: T
    ) -> T:
        ...

    async def get_by_id(
        self,
        entity_id: UUID
    ) -> T | None:
        ...

    async def list(
        self,
        filters: FilterParams | None = None,
        pagination: PaginationParams | None = None,
        sorting: SortParams | None = None,
    ) -> list[T]:
        ...

    async def update(
        self,
        entity: T
    ) -> T:
        ...

    async def delete(
        self,
        entity_id: UUID
    ) -> None:
        ...

    async def count(
        self,
        filters: FilterParams | None = None
    ) -> int:
        ...