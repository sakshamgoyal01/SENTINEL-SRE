from typing import Type

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from backend.auth.dependencies import (
    RequireViewer,
)

from backend.repositories.pagination import (
    PaginationParams,
)


class ReadOnlyRouter:

    def __init__(
        self,
        *,
        service_dependency,
        response_schema: Type,
        prefix: str,
        tags: list[str],
    ):

        self.router = APIRouter(
            prefix=prefix,
            tags=tags,
        )

        self.response_schema = (
            response_schema
        )

        self.service_dependency = (
            service_dependency
        )

        self._register_routes()

    def _register_routes(
        self,
    ):

        router = self.router

        @router.get(
            "/",
            dependencies=[
                Depends(
                    RequireViewer
                )
            ],
        )
        async def list_entities(
            page: int = 1,
            page_size: int = 50,
            service=Depends(
                self.service_dependency
            ),
        ):

            pagination = (
                PaginationParams(
                    page=page,
                    page_size=page_size,
                )
            )

            return await (
                service.list(
                    pagination
                )
            )

        @router.get(
            "/{entity_id}",
            dependencies=[
                Depends(
                    RequireViewer
                )
            ],
        )
        async def get_entity(
            entity_id: str,
            service=Depends(
                self.service_dependency
            ),
        ):

            entity = await (
                service.get(
                    entity_id
                )
            )

            if entity is None:

                raise HTTPException(
                    status_code=
                    status.HTTP_404_NOT_FOUND,
                    detail=
                    "Entity not found",
                )

            return entity