from datetime import datetime

from pydantic import BaseModel

from ai.models.root_cause import (
    RootCause
)

from ai.models.causal_chain import (
    CausalChain
)


class RootCauseResult(BaseModel):

    rootcause_id: str

    investigation_id: str

    service: str

    severity: str

    priority: str

    root_cause: RootCause

    causal_chain: CausalChain

    evidence: list[str]

    confidence: float

    generated_at: datetime