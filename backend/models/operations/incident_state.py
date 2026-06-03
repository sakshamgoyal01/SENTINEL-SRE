from sqlalchemy import (
    String,
    DateTime
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


class IncidentState(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin
):
    __tablename__ = "incident_states"

    incident_id: Mapped[str] = mapped_column(
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

    current_state: Mapped[str] = (
        mapped_column(
            String(100),
            nullable=False,
            index=True
        )
    )

    source_topic: Mapped[str] = (
        mapped_column(
            String(255),
            nullable=False
        )
    )

    updated_at_event: Mapped[DateTime] = (
        mapped_column(
            DateTime(timezone=True),
            nullable=False
        )
    )