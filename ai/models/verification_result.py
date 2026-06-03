from datetime import datetime

from pydantic import BaseModel

from ai.models.verification_check import (
    VerificationCheck
)


class VerificationResult(
    BaseModel
):

    verification_id: str

    execution_id: str

    service: str

    verified: bool

    health_status: str

    verification_result: str

    checks: list[
        VerificationCheck
    ]

    generated_at: datetime