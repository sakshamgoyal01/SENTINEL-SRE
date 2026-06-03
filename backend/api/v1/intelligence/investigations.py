from backend.api.crud_router import CRUDRouter
from backend.api.dependencies.investigation import get_investigation_service
from backend.schemas.intelligence.investigation import (
    InvestigationResponse,
    CreateInvestigationRequest,
    UpdateInvestigationRequest,
)

router = CRUDRouter(
    service_dependency=get_investigation_service,
    response_schema=InvestigationResponse,
    create_schema=CreateInvestigationRequest,
    update_schema=UpdateInvestigationRequest,
    prefix="",
    tags=["Investigations"],
).router