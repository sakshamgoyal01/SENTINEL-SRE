from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.database.base import Base
from backend.database.mixins import (
    UUIDMixin,
    TimestampMixin,
)

class Metric(
    Base,
    UUIDMixin,
    TimestampMixin
):
    __tablename__ = "metrics"

    event_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )

    timestamp: Mapped[str] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        index=True
    )

    source: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    service: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    metric_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True
    )

    value: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    labels: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
        default=dict
    )

    unit: Mapped[str | None] = mapped_column(
        String(50)
    )

    cluster: Mapped[str | None] = mapped_column(
        String(255),
        index=True
    )

    environment: Mapped[str | None] = mapped_column(
        String(255),
        index=True
    )

    namespace: Mapped[str | None] = mapped_column(
        String(255),
        index=True
    )