from datetime import datetime

from ai.models.incident_state import (
    IncidentState
)


class StateManager:

    def update(

        self,

        incident_id: str,

        service: str,

        state: str,

        topic: str
    ):

        return IncidentState(

            incident_id=
            incident_id,

            service=
            service,

            current_state=
            state,

            source_topic=
            topic,

            updated_at=
            datetime.utcnow()
        )