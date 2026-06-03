import uuid

from sqlalchemy import DateTime
from sqlalchemy import func

from sqlalchemy.orm import mapped_column

from sqlalchemy.dialects.postgresql import UUID


class UUIDMixin:

    id = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )


class TimestampMixin:

    created_at = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    updated_at = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )


class TenantMixin:

    tenant_id = mapped_column(
        UUID(as_uuid=True),
        nullable=True,
        index=True
    )


class AuditMixin:

    created_by = mapped_column(
        UUID(as_uuid=True),
        nullable=True
    )

    updated_by = mapped_column(
        UUID(as_uuid=True),
        nullable=True
    )