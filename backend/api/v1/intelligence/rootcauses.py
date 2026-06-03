from backend.api.crud_router import CRUDRouter
from backend.api.dependencies.rootcause import get_rootcause_service
from backend.schemas.intelligence.rootcause import (
    RootCauseResponse,
    CreateRootCauseRequest,
    UpdateRootCauseRequest,
)

router = CRUDRouter(
    service_dependency=get_rootcause_service,
    response_schema=RootCauseResponse,
    create_schema=CreateRootCauseRequest,
    update_schema=UpdateRootCauseRequest,
    prefix="",
    tags=["Root Causes"],
).router