from backend.api.crud_router import CRUDRouter
from backend.api.dependencies.remediation import get_remediation_service
from backend.schemas.intelligence.remediation import (
    RemediationResponse,
    CreateRemediationRequest,
    UpdateRemediationRequest,
)

router = CRUDRouter(
    service_dependency=get_remediation_service,
    response_schema=RemediationResponse,
    create_schema=CreateRemediationRequest,
    update_schema=UpdateRemediationRequest,
    prefix="",
    tags=["Remediations"],
).router