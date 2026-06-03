from backend.api.crud_router import (
    CRUDRouter
)

from backend.api.dependencies.audit import (
    get_audit_service
)

from backend.schemas.operations.audit import (
    AuditResponse,
    CreateAuditRequest,
    UpdateAuditRequest,
)

router = CRUDRouter(
    service_dependency=get_audit_service,
    response_schema=AuditResponse,
    create_schema=CreateAuditRequest,
    update_schema=UpdateAuditRequest,
    prefix="",
    tags=["Execution Audits"],
).router