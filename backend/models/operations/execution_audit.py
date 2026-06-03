from sqlalchemy import (
    String
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


class ExecutionAudit(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin
):
    __tablename__ = "execution_audits"

    audit_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    service: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    approval_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True
    )

    execution_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True
    )

    verification_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True
    )

    recovery_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True
    )

    status: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    details: Mapped[str] = mapped_column(
        String(1000),
        nullable=False
    )