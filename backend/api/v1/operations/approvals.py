from backend.api.crud_router import (
    CRUDRouter
)

from backend.api.dependencies.approvals import (
    get_approval_service
)

from backend.schemas.operations.approval import (
    ApprovalResponse,
    CreateApprovalRequest,
    UpdateApprovalRequest,
)

router = CRUDRouter(
    service_dependency=
        get_approval_service,

    response_schema=
        ApprovalResponse,

    create_schema=
        CreateApprovalRequest,

    update_schema=
        UpdateApprovalRequest,

    prefix="",

    tags=[
        "Approvals"
    ],
).router