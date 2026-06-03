from pydantic import BaseModel


class RecoveryStrategy(
    BaseModel
):

    strategy_type: str

    confidence: float

    reason: str