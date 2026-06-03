from datetime import datetime

from pydantic import BaseModel

from ai.models.execution_action import (
    ExecutionAction
)


class ExecutionResult(BaseModel):

    execution_id: str

    service: str

    executed: bool

    status: str

    mode: str

    actions: list[ExecutionAction]

    generated_at: datetime