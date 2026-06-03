from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.telemetry.kubernetes_event import (
    KubernetesEvent
)

from backend.repositories.base_repository import (
    BaseRepository
)


class KubernetesRepository(
    BaseRepository[KubernetesEvent]
):

    def __init__(
        self,
        session: AsyncSession
    ):
        super().__init__(
            session=session,
            model=KubernetesEvent
        )