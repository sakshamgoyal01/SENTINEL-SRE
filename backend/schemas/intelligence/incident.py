from pydantic import BaseModel


class CreateIncidentRequest(
    BaseModel
):

    incident_id: str

    service: str

    severity: str

    priority: str

    category: str

    summary: str


class UpdateIncidentRequest(
    BaseModel
):

    severity: str | None = None

    priority: str | None = None

    summary: str | None = None


class IncidentResponse(
    BaseModel
):

    id: str

    incident_id: str

    service: str

    severity: str

    priority: str

    category: str

    summary: str

    model_config = {
        "from_attributes": True
    }