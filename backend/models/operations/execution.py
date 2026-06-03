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


class Execution(
    Base,
    UUIDMixin,
    TimestampMixin,
    TenantMixin
):
    __tablename__ = "executions"

    execution_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    approval_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True
    )

    service: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    executed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    mode: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    actions: Mapped[list] = mapped_column(
        JSONB,
        nullable=False
    )