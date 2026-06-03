from sqlalchemy import (
    String,
    Float,
    DateTime
)
from datetime import datetime
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


class ProcessedTelemetry(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin
):
    __tablename__ = (
        "processed_telemetry"
    )

    event_id: Mapped[str] = (
        mapped_column(
            String(255),
            unique=True,
            index=True,
            nullable=False,
        )
    )

    event_type: Mapped[str] = (
        mapped_column(
            String(50),
            nullable=False,
            index=True,
        )
    )

    category: Mapped[str] = (
        mapped_column(
            String(100),
            nullable=False,
            index=True,
        )
    )

    severity: Mapped[str] = (
        mapped_column(
            String(50),
            nullable=False,
            index=True,
        )
    )

    priority: Mapped[str] = (
        mapped_column(
            String(20),
            nullable=False,
            index=True,
        )
    )

    risk_score: Mapped[float] = (
        mapped_column(
            Float,
            nullable=False,
        )
    )

    service: Mapped[str] = (
        mapped_column(
            String(255),
            nullable=False,
            index=True,
        )
    )

    summary: Mapped[str] = (
        mapped_column(
            String(2000),
            nullable=False,
        )
    )

    raw_event: Mapped[dict] = (
        mapped_column(
            JSONB,
            nullable=False,
            default=dict,
        )
    )

    created_at_event: Mapped[datetime | None] = (
        mapped_column(
            DateTime(timezone=True),
            nullable=True,
            index=True,
        )
    )