from pydantic import BaseModel


class StateTransition(
    BaseModel
):

    from_state: str

    to_state: str

    reason: str