from backend.api.crud_router import CRUDRouter

from backend.api.dependencies.trace import (
    get_trace_service
)

from backend.schemas.telemetry.trace import (
    TraceResponse,
    CreateTraceRequest,
    UpdateTraceRequest,
)

router = CRUDRouter(
    service_dependency=get_trace_service,
    response_schema=TraceResponse,
    create_schema=CreateTraceRequest,
    update_schema=UpdateTraceRequest,
    prefix="",
    tags=["Traces"],
).router