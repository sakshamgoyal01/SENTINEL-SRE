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


class RolePermission(
    Base,
    UUIDMixin,
    TimestampMixin
):
    __tablename__ = (
        "role_permissions"
    )

    role_id: Mapped[str] = (
        mapped_column(
            String(255),
            nullable=False,
            index=True
        )
    )

    permission_id: Mapped[str] = (
        mapped_column(
            String(255),
            nullable=False,
            index=True
        )
    )