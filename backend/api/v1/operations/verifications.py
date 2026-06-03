from backend.api.crud_router import (
    CRUDRouter
)

from backend.api.dependencies.verification import (
    get_verification_service
)

from backend.schemas.operations.verification import (
    VerificationResponse,
    CreateVerificationRequest,
    UpdateVerificationRequest,
)

router = CRUDRouter(
    service_dependency=get_verification_service,
    response_schema=VerificationResponse,
    create_schema=CreateVerificationRequest,
    update_schema=UpdateVerificationRequest,
    prefix="",
    tags=["Verifications"],
).router