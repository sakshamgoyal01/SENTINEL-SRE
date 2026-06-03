from backend.models.intelligence.alert import (
    Alert
)

from backend.repositories.base_repository import (
    BaseRepository
)


class AlertRepository(
    BaseRepository[Alert]
):

    def __init__(
        self,
        session,
    ):
        super().__init__(
            session=session,
            model=Alert,
        )