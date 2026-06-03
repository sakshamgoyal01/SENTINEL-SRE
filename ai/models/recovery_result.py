from datetime import datetime

from pydantic import BaseModel

from ai.models.recovery_strategy import (
    RecoveryStrategy
)


class RecoveryResult(
    BaseModel
):

    recovery_id: str

    verification_id: str

    service: str

    recovery_status: str

    strategy: RecoveryStrategy

    generated_at: datetime