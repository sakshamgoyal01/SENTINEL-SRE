from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.database.base import Base
from backend.database.mixins import (
    UUIDMixin,
    TimestampMixin
)

class Log(
    Base,
    UUIDMixin,
    TimestampMixin
):
    __tablename__ = "logs"

    event_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True
    )

    timestamp: Mapped[str] = mapped_column(
        DateTime(timezone=True),
        index=True
    )

    service: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    severity: Mapped[str] = mapped_column(
        String(50),
        index=True
    )

    message: Mapped[str] = mapped_column(
        Text
    )

    trace_id: Mapped[str | None] = mapped_column(
        String(255),
        index=True
    )

    span_id: Mapped[str | None] = mapped_column(
        String(255)
    )

    logger: Mapped[str | None] = mapped_column(
        String(255)
    )