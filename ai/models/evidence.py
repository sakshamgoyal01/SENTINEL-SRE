from pydantic import BaseModel


class Evidence(BaseModel):

    evidence_type: str

    source: str

    description: str

    confidence: float = 1.0