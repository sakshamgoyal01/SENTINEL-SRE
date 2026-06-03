from datetime import datetime

from pydantic import BaseModel


class IncidentState(
    BaseModel
):

    incident_id: str

    service: str

    current_state: str

    source_topic: str

    updated_at: datetime