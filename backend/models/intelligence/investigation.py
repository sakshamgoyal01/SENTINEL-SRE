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


class Investigation(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin
):
    __tablename__ = "investigations"

    investigation_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    incident_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True
    )

    service: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    severity: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    priority: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    findings: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False
    )

    evidence: Mapped[list] = mapped_column(
        JSONB,
        nullable=False
    )

    confidence: Mapped[float] = mapped_column(
        nullable=False
    )