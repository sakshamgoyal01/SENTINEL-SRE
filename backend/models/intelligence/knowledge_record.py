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


class KnowledgeRecord(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin
):
    __tablename__ = "knowledge_records"

    knowledge_id: Mapped[str] = mapped_column(
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

    pattern: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False
    )

    remediation: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False
    )

    source_incident_type: Mapped[str | None] = (
        mapped_column(
            String(100),
            nullable=True
        )
    )

    success_rate: Mapped[float | None] = (
        mapped_column(
            nullable=True
        )
    )

    created_at_event: Mapped[DateTime] = (
        mapped_column(
            DateTime(timezone=True),
            nullable=False
        )
    )