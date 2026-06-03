from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import Base
from backend.database.mixins import (
    UUIDMixin,
    TimestampMixin,
    TenantMixin,
)


class Remediation(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin,
):
    __tablename__ = "remediations"

    remediation_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    risk_id: Mapped[str] = mapped_column(
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
    )

    plan: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )