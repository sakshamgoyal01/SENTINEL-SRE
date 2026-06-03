from sqlalchemy import (
    String,
    Boolean
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


class Verification(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin
):
    __tablename__ = "verifications"

    verification_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    execution_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    service: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    health_status: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    verification_result: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    checks: Mapped[list] = mapped_column(
        JSONB,
        nullable=False
    )