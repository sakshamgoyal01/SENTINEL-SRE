from backend.api.read_only_router import (
    ReadOnlyRouter
)

from backend.api.dependencies.dlq import (
    get_dead_letter_service
)

from backend.schemas.system.dlq import (
    DeadLetterRecordResponse
)

router = ReadOnlyRouter(
    service_dependency=get_dead_letter_service,
    response_schema=DeadLetterRecordResponse,
    prefix="",
    tags=["DLQ"],
).router