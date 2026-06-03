from datetime import datetime

from pydantic import BaseModel


class DeadLetterRecordResponse(BaseModel):
    id: str
    dlq_id: str
    source_topic: str
    payload: dict
    error_message: str
    failed_at: datetime | None

    model_config = {
        "from_attributes": True
    }