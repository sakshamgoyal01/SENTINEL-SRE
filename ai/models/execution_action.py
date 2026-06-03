from pydantic import BaseModel


class ExecutionAction(BaseModel):

    action_type: str

    target: str

    mode: str