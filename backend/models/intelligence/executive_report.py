from sqlalchemy import (
    String,
    DateTime
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


class ExecutiveReport(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin
):
    __tablename__ = "executive_reports"

    report_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    service: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    summary: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False
    )

    generated_at: Mapped[DateTime] = (
        mapped_column(
            DateTime(timezone=True),
            nullable=False
        )
    )