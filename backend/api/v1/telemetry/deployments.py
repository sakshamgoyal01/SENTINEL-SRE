from backend.api.crud_router import CRUDRouter

from backend.api.dependencies.deployment import (
    get_deployment_service
)

from backend.schemas.telemetry.deployment import (
    DeploymentResponse,
    CreateDeploymentRequest,
    UpdateDeploymentRequest,
)

router = CRUDRouter(
    service_dependency=get_deployment_service,
    response_schema=DeploymentResponse,
    create_schema=CreateDeploymentRequest,
    update_schema=UpdateDeploymentRequest,
    prefix="",
    tags=["Deployments"],
).router