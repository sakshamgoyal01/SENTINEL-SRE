from typing import List, Optional

from pydantic import BaseModel

from processing.models.operational_event import (
    OperationalEvent
)


class ProcessingResult(BaseModel):

    success: bool

    event: Optional[OperationalEvent] = None

    errors: List[str] = []

    warnings: List[str] = []