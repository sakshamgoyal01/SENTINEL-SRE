from backend.api.crud_router import (
    CRUDRouter
)

from backend.api.dependencies.escalation import (
    get_escalation_service
)

from backend.schemas.operations.escalation import (
    EscalationResponse,
    CreateEscalationRequest,
    UpdateEscalationRequest,
)

router = CRUDRouter(
    service_dependency=get_escalation_service,
    response_schema=EscalationResponse,
    create_schema=CreateEscalationRequest,
    update_schema=UpdateEscalationRequest,
    prefix="",
    tags=["Escalations"],
).router