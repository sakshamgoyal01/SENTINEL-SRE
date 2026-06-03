from backend.api.crud_router import CRUDRouter

from backend.api.dependencies.log import (
    get_log_service
)

from backend.schemas.telemetry.log import (
    LogResponse,
    CreateLogRequest,
    UpdateLogRequest,
)

router = CRUDRouter(
    service_dependency=get_log_service,
    response_schema=LogResponse,
    create_schema=CreateLogRequest,
    update_schema=UpdateLogRequest,
    prefix="",
    tags=["Logs"],
).router