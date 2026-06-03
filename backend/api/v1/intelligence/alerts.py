from backend.api.crud_router import (
    CRUDRouter
)

from backend.api.dependencies.alerts import (
    get_alert_service
)

from backend.schemas.intelligence.alert import (
    AlertResponse,
    CreateAlertRequest,
    UpdateAlertRequest,
)

router = CRUDRouter(
    service_dependency=
        get_alert_service,

    response_schema=
        AlertResponse,

    create_schema=
        CreateAlertRequest,

    update_schema=
        UpdateAlertRequest,

    prefix="",

    tags=[
        "Alerts"
    ],
).router