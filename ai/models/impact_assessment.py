from pydantic import BaseModel


class ImpactAssessment(BaseModel):

    customer_impact: str

    business_impact: str

    operational_impact: str