from sqlalchemy import (
    String
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


class UserRole(
    Base,
    UUIDMixin,
    TimestampMixin
):
    __tablename__ = "user_roles"

    user_id: Mapped[str] = (
        mapped_column(
            String(255),
            nullable=False,
            index=True
        )
    )

    role_id: Mapped[str] = (
        mapped_column(
            String(255),
            nullable=False,
            index=True
        )
    )