from pydantic import BaseModel


class CreateMetricRequest(BaseModel):
    service: str
    source: str
    metric_name: str
    value: float
    labels: dict | None = None
    cluster: str | None = None
    environment: str | None = None
    namespace: str | None = None


class UpdateMetricRequest(BaseModel):
    value: float | None = None
    labels: dict | None = None


class MetricResponse(BaseModel):
    id: str
    service: str
    source: str
    metric_name: str
    value: float
    labels: dict | None

    model_config = {
        "from_attributes": True
    }