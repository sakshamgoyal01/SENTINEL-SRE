from pydantic import BaseModel


class CreateAlertRequest(
    BaseModel
):

    alert_id: str

    service: str

    severity: str

    title: str

    description: str

    status: str

    source: str


class UpdateAlertRequest(
    BaseModel
):

    status: str | None = None

    description: str | None = None


class AlertResponse(
    BaseModel
):

    id: str

    alert_id: str

    service: str

    severity: str

    title: str

    description: str

    status: str

    source: str

    model_config = {
        "from_attributes": True
    }