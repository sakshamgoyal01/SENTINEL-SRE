from backend.api.crud_router import (
    CRUDRouter
)

from backend.api.dependencies.incidents import (
    get_incident_service
)

from backend.schemas.intelligence.incident import (
    IncidentResponse,
    CreateIncidentRequest,
    UpdateIncidentRequest,
)

router = CRUDRouter(
    service_dependency=
        get_incident_service,

    response_schema=
        IncidentResponse,

    create_schema=
        CreateIncidentRequest,

    update_schema=
        UpdateIncidentRequest,

    prefix="",

    tags=[
        "Incidents"
    ],
).router