from sqlalchemy import (
    String,
    Text
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


class Permission(
    Base,
    UUIDMixin,
    TimestampMixin
):
    __tablename__ = "permissions"

    name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    description: Mapped[
        str | None
    ] = mapped_column(
        Text,
        nullable=True
    )