from sqlalchemy import (
    String,
    Boolean,
    DateTime,
    Text
)
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB

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


class Approval(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin
):
    __tablename__ = "approvals"

    approval_id: Mapped[str] = mapped_column(
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

    approved: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    requires_human_approval: Mapped[bool] = (
        mapped_column(
            Boolean,
            nullable=False
        )
    )

    reason: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    actions: Mapped[list] = mapped_column(
        JSONB,
        nullable=False
    )

    generated_at: Mapped[datetime] = (
        mapped_column(
            DateTime(timezone=True),
            nullable=False
        )
    )

