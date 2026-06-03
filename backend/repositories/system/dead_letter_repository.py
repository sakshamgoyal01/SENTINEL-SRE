from backend.models.system.dead_letter_record import (
    DeadLetterRecord
)

from backend.repositories.base_repository import (
    BaseRepository
)


class DeadLetterRepository(
    BaseRepository[DeadLetterRecord]
):

    def __init__(
        self,
        session,
    ):
        super().__init__(
            session=session,
            model=DeadLetterRecord,
        )