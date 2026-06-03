from pydantic import BaseModel


class IncidentPattern(BaseModel):

    incident_type: str

    service: str

    severity: str

    root_cause: str