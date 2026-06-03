from sqlalchemy import (
    String,
    Integer,
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


class AggregatedEvent(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin
):
    __tablename__ = (
        "aggregated_events"
    )

    aggregation_key: Mapped[str] = (
        mapped_column(
            String(255),
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

    count: Mapped[int] = (
        mapped_column(
            Integer,
            nullable=False,
        )
    )

    services: Mapped[list] = (
        mapped_column(
            JSONB,
            nullable=False,
            default=list,
        )
    )

    summary: Mapped[str] = (
        mapped_column(
            String(2000),
            nullable=False,
        )
    )

    created_at_event: Mapped[datetime | None] = (
        mapped_column(
            DateTime(timezone=True),
            nullable=True,
            index=True,
        )
    )