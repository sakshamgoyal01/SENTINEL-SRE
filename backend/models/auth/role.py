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


class Role(
    Base,
    UUIDMixin,
    TimestampMixin
):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(
        String(100),
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