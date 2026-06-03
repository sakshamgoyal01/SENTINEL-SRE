from backend.api.crud_router import CRUDRouter

from backend.api.dependencies.kubernetes import (
    get_kubernetes_service
)

from backend.schemas.telemetry.kubernetes import (
    KubernetesResponse,
    CreateKubernetesRequest,
    UpdateKubernetesRequest,
)

router = CRUDRouter(
    service_dependency=get_kubernetes_service,
    response_schema=KubernetesResponse,
    create_schema=CreateKubernetesRequest,
    update_schema=UpdateKubernetesRequest,
    prefix="",
    tags=["Kubernetes"],
).router