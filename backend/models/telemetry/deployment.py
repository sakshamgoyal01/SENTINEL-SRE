from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.database.base import Base
from backend.database.mixins import (
    UUIDMixin,
    TimestampMixin
)

class Deployment(
    Base,
    UUIDMixin,
    TimestampMixin
):
    __tablename__ = "deployments"

    timestamp: Mapped[str] = mapped_column(
        DateTime(timezone=True),
        index=True
    )

    deployment_name: Mapped[str] = (
        mapped_column(
            String(255),
            index=True
        )
    )

    namespace: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    image: Mapped[str | None] = mapped_column(
        String(500)
    )

    replicas: Mapped[int] = mapped_column(
        Integer
    )

    available_replicas: Mapped[int | None] = (
        mapped_column(
            Integer
        )
    )

    updated_replicas: Mapped[int | None] = (
        mapped_column(
            Integer
        )
    )

    strategy: Mapped[str | None] = (
        mapped_column(
            String(100)
        )
    )