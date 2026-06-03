from backend.api.crud_router import (
    CRUDRouter
)

from backend.api.dependencies.recovery import (
    get_recovery_service
)

from backend.schemas.operations.recovery import (
    RecoveryResponse,
    CreateRecoveryRequest,
    UpdateRecoveryRequest,
)

router = CRUDRouter(
    service_dependency=get_recovery_service,
    response_schema=RecoveryResponse,
    create_schema=CreateRecoveryRequest,
    update_schema=UpdateRecoveryRequest,
    prefix="",
    tags=["Recoveries"],
).router