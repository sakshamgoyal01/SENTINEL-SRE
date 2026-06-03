from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import DateTime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.database.base import Base
from backend.database.mixins import (
    UUIDMixin,
    TimestampMixin
)

class Trace(
    Base,
    UUIDMixin,
    TimestampMixin
):
    __tablename__ = "traces"

    timestamp: Mapped[str] = mapped_column(
        DateTime(timezone=True),
        index=True
    )

    trace_id: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    span_id: Mapped[str] = mapped_column(
        String(255)
    )

    parent_span_id: Mapped[str | None] = mapped_column(
        String(255)
    )

    service: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    operation: Mapped[str] = mapped_column(
        String(255)
    )

    duration_ms: Mapped[float] = mapped_column(
        Float
    )

    status_code: Mapped[int | None] = mapped_column(
        Integer
    )