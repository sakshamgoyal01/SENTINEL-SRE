from sqlalchemy import (
    String
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


class Recovery(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin
):
    __tablename__ = "recoveries"

    recovery_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    verification_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    service: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    recovery_status: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    strategy: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False
    )