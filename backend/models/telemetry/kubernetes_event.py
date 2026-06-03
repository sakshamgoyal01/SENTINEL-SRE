from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.database.base import Base
from backend.database.mixins import (
    UUIDMixin,
    TimestampMixin
)

class KubernetesEvent(
    Base,
    UUIDMixin,
    TimestampMixin
):
    __tablename__ = "kubernetes_events"

    timestamp: Mapped[str] = mapped_column(
        DateTime(timezone=True),
        index=True
    )

    reason: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    message: Mapped[str] = mapped_column(
        Text
    )

    event_type: Mapped[str] = mapped_column(
        String(100),
        index=True
    )

    involved_object: Mapped[dict] = (
        mapped_column(
            JSONB
        )
    )