from pydantic import BaseModel


class RootCause(BaseModel):

    category: str

    probable_cause: str

    confidence: float