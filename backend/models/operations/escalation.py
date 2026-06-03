from sqlalchemy import (
    String
)

from sqlalchemy.dialects.postgresql import (
    JSONB
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from backend.database.base import Base
from backend.database.mixins import (
    UUIDMixin,
    TimestampMixin,
    TenantMixin
)


class Escalation(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin
):
    __tablename__ = "escalations"

    escalation_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    recovery_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    service: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    escalation_reason: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    target: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False
    )