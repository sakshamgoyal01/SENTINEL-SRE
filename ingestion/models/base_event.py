from uuid import uuid4

from datetime import datetime

from pydantic import BaseModel, Field

from ingestion.models.metadata import Metadata

from ingestion.models.enums import EventSource


class BaseEvent(BaseModel):

    event_id: str = Field(
        default_factory=lambda: str(uuid4())
    )

    timestamp: datetime

    source: EventSource

    version: str = "v1"

    metadata: Metadata