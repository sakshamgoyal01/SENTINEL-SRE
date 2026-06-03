from pydantic import BaseModel


class CreateDeploymentRequest(BaseModel):
    service: str
    deployment_id: str
    version: str
    environment: str
    status: str


class UpdateDeploymentRequest(BaseModel):
    status: str | None = None


class DeploymentResponse(BaseModel):
    id: str
    deployment_id: str
    service: str
    version: str
    environment: str
    status: str

    model_config = {
        "from_attributes": True
    }