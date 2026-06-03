from sqlalchemy import (
    String,
    Float,
    Boolean,
    Index
)

from sqlalchemy.dialects.postgresql import (
    JSONB
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from backend.database.base import Base
from backend.database.mixins import (
    UUIDMixin,
    TimestampMixin,
    TenantMixin
)


class Incident(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin
):
    __tablename__ = "incidents"

    service: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    incident_priority: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        index=True
    )

    impact_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    final_risk_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    requires_human_review: Mapped[bool] = (
        mapped_column(
            Boolean,
            nullable=False,
            default=False
        )
    )

    escalation_required: Mapped[bool] = (
        mapped_column(
            Boolean,
            nullable=False,
            default=False
        )
    )

    aggregated_event: Mapped[dict] = (
        mapped_column(
            JSONB,
            nullable=False
        )
    )


Index(
    "idx_incident_service_priority",
    Incident.service,
    Incident.incident_priority
)