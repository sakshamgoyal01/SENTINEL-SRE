from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.telemetry.deployment import (
    Deployment
)

from backend.repositories.base_repository import (
    BaseRepository
)


class DeploymentRepository(
    BaseRepository[Deployment]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=Deployment
        )