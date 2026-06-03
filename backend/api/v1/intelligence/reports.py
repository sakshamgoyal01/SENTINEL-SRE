from backend.api.read_only_router import (
    ReadOnlyRouter
)

from backend.api.dependencies.report import (
    get_report_service
)

from backend.schemas.intelligence.report import (
    ExecutiveReportResponse
)

router = ReadOnlyRouter(
    service_dependency=get_report_service,
    response_schema=ExecutiveReportResponse,
    prefix="",
    tags=["Reports"],
).router