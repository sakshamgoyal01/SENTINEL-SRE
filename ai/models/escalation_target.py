from pydantic import BaseModel


class EscalationTarget(
    BaseModel
):

    team: str

    severity: str

    contact_channel: str