from backend.api.read_only_router import (
    ReadOnlyRouter
)

from backend.api.dependencies.processed_telemetry import (
    get_processed_telemetry_service
)

from backend.schemas.telemetry.processed_telemetry import (
    ProcessedTelemetryResponse
)

router = ReadOnlyRouter(
    service_dependency=get_processed_telemetry_service,
    response_schema=ProcessedTelemetryResponse,
    prefix="",
    tags=["Processed Telemetry"],
).router