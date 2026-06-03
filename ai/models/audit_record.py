from datetime import datetime

from pydantic import BaseModel


class AuditRecord(
    BaseModel
):

    audit_id: str

    service: str

    approval_id: str | None

    execution_id: str | None

    verification_id: str | None

    recovery_id: str | None

    status: str

    details: str

    created_at: datetime