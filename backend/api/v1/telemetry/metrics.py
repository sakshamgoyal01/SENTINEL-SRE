from backend.api.crud_router import (
    CRUDRouter
)

from backend.api.dependencies.metric import (
    get_metric_service
)

from backend.schemas.telemetry.metric import (
    MetricResponse,
    CreateMetricRequest,
    UpdateMetricRequest,
)

router = CRUDRouter(
    service_dependency=get_metric_service,
    response_schema=MetricResponse,
    create_schema=CreateMetricRequest,
    update_schema=UpdateMetricRequest,
    prefix="",
    tags=["Metrics"],
).router