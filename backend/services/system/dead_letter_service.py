from backend.services.base_service import (
    BaseService
)

from backend.models.system.dead_letter_record import (
    DeadLetterRecord
)


class DeadLetterService(
    BaseService
):

    async def create_from_event(
        self,
        payload: dict,
    ) -> DeadLetterRecord:

        entity = DeadLetterRecord(
            dlq_id=payload[
                "dlq_id"
            ],
            source_topic=payload[
                "source_topic"
            ],
            payload=payload[
                "payload"
            ],
            error_message=payload[
                "error_message"
            ],
            failed_at=payload.get(
                "failed_at"
            ),
        )

        return await (
            self.repository.create(
                entity
            )
        )