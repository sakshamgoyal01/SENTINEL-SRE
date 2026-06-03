from sqlalchemy import (
    String,
    DateTime
)
from datetime import datetime
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
    TimestampMixin
)


class DeadLetterRecord(
    Base,
    UUIDMixin,
    TimestampMixin
):
    __tablename__ = (
        "dead_letter_records"
    )

    dlq_id: Mapped[str] = (
        mapped_column(
            String(255),
            unique=True,
            nullable=False,
            index=True,
        )
    )

    source_topic: Mapped[str] = (
        mapped_column(
            String(255),
            nullable=False,
            index=True,
        )
    )

    payload: Mapped[dict] = (
        mapped_column(
            JSONB,
            nullable=False,
        )
    )

    error_message: Mapped[str] = (
        mapped_column(
            String(5000),
            nullable=False,
        )
    )

    failed_at: Mapped[datetime | None] = (
        mapped_column(
            DateTime(timezone=True),
            nullable=True,
            index=True,
        )
    )