from pydantic import BaseModel


class RiskSummary(BaseModel):

    risk_level: str

    estimated_mttr_minutes: int

    slo_risk_percent: float