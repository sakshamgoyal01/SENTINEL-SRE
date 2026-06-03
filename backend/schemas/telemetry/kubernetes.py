from pydantic import BaseModel


class CreateKubernetesRequest(BaseModel):
    service: str
    event_type: str
    resource_kind: str
    resource_name: str
    namespace: str


class UpdateKubernetesRequest(BaseModel):
    event_type: str | None = None


class KubernetesResponse(BaseModel):
    id: str
    service: str
    event_type: str
    resource_kind: str
    resource_name: str
    namespace: str

    model_config = {
        "from_attributes": True
    }