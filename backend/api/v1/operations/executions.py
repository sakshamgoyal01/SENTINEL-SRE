from backend.api.crud_router import (
    CRUDRouter
)

from backend.api.dependencies.execution import (
    get_execution_service
)

from backend.schemas.operations.execution import (
    ExecutionResponse,
    CreateExecutionRequest,
    UpdateExecutionRequest,
)

router = CRUDRouter(
    service_dependency=get_execution_service,
    response_schema=ExecutionResponse,
    create_schema=CreateExecutionRequest,
    update_schema=UpdateExecutionRequest,
    prefix="",
    tags=["Executions"],
).router