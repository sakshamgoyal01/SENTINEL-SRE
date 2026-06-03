from sqlalchemy import (
    String,
    DateTime
)
from datetime import datetime
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


class Alert(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin
):
    __tablename__ = "alerts"

    alert_id: Mapped[str] = (
        mapped_column(
            String(255),
            unique=True,
            nullable=False,
            index=True,
        )
    )

    service: Mapped[str] = (
        mapped_column(
            String(255),
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

    title: Mapped[str] = (
        mapped_column(
            String(500),
            nullable=False,
        )
    )

    description: Mapped[str] = (
        mapped_column(
            String(5000),
            nullable=False,
        )
    )

    status: Mapped[str] = (
        mapped_column(
            String(50),
            nullable=False,
            index=True,
        )
    )

    source: Mapped[str] = (
        mapped_column(
            String(255),
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