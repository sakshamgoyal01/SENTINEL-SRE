from backend.api.crud_router import (
    CRUDRouter
)

from backend.api.dependencies.risks import (
    get_risk_service
)

from backend.schemas.intelligence.risk import (
    RiskResponse,
    CreateRiskRequest,
    UpdateRiskRequest,
)

router = CRUDRouter(
    service_dependency=
        get_risk_service,

    response_schema=
        RiskResponse,

    create_schema=
        CreateRiskRequest,

    update_schema=
        UpdateRiskRequest,

    prefix="",

    tags=[
        "Risks"
    ],
).router