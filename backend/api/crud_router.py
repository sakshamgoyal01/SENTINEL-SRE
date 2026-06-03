from typing import Type

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from backend.auth.dependencies import (
    RequireViewer,
    RequireSRE,
    RequireAdmin,
)

from backend.repositories.pagination import (
    PaginationParams
)


class CRUDRouter:

    def __init__(
        self,
        *,
        service_dependency,
        response_schema: Type,
        create_schema: Type,
        update_schema: Type,
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

        self.create_schema = (
            create_schema
        )

        self.update_schema = (
            update_schema
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

        @router.post(
            "/",
            dependencies=[
                Depends(
                    RequireSRE
                )
            ],
        )
        async def create_entity(
            payload: self.create_schema,
            service=Depends(
                self.service_dependency
            ),
        ):

            entity = (
                service.repository.model(
                    **payload.model_dump()
                )
            )

            result = await (
                service.create(
                    entity
                )
            )

            await (
                service.repository.session.commit()
            )

            return result

        @router.patch(
            "/{entity_id}",
            dependencies=[
                Depends(
                    RequireSRE
                )
            ],
        )
        async def update_entity(
            entity_id: str,
            payload: self.update_schema,
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

            updates = (
                payload.model_dump(
                    exclude_unset=True
                )
            )

            for (
                key,
                value
            ) in updates.items():

                setattr(
                    entity,
                    key,
                    value,
                )

            result = await (
                service.update(
                    entity
                )
            )

            await (
                service.repository.session.commit()
            )

            return result

        @router.delete(
            "/{entity_id}",
            dependencies=[
                Depends(
                    RequireAdmin
                )
            ],
        )
        async def delete_entity(
            entity_id: str,
            service=Depends(
                self.service_dependency
            ),
        ):

            exists = await (
                service.exists(
                    entity_id
                )
            )

            if not exists:

                raise HTTPException(
                    status_code=
                    status.HTTP_404_NOT_FOUND,
                    detail=
                    "Entity not found",
                )

            await (
                service.delete(
                    entity_id
                )
            )

            await (
                service.repository.session.commit()
            )

            return {
                "status": "deleted",
                "id": entity_id,
            }