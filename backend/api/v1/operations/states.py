from backend.api.crud_router import (
    CRUDRouter
)

from backend.api.dependencies.incident_state import (
    get_incident_state_service
)

from backend.schemas.operations.incident_state import (
    IncidentStateResponse,
    CreateIncidentStateRequest,
    UpdateIncidentStateRequest,
)

router = CRUDRouter(
    service_dependency=get_incident_state_service,
    response_schema=IncidentStateResponse,
    create_schema=CreateIncidentStateRequest,
    update_schema=UpdateIncidentStateRequest,
    prefix="",
    tags=["Incident States"],
).router