from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import Base
from backend.database.mixins import (
    UUIDMixin,
    TimestampMixin,
    TenantMixin,
)


class Risk(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin,
):
    __tablename__ = "risks"

    risk_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    rootcause_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    service: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    priority: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        index=True,
    )

    blast_radius: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )

    impact_assessment: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )

    risk_summary: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )