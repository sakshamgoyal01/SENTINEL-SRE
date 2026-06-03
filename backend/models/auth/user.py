from datetime import datetime

from sqlalchemy import (
    String,
    Boolean,
    DateTime
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


class User(
    Base,
    UUIDMixin,
    TimestampMixin
):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    username: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash: Mapped[str] = (
        mapped_column(
            String(500),
            nullable=False
        )
    )

    is_active: Mapped[bool] = (
        mapped_column(
            Boolean,
            nullable=False,
            default=True
        )
    )

    is_superuser: Mapped[bool] = (
        mapped_column(
            Boolean,
            nullable=False,
            default=False
        )
    )

    last_login: Mapped[
        datetime | None
    ] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )