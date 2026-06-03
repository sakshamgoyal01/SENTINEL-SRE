from pydantic import BaseModel


class BlastRadius(BaseModel):

    impacted_services: list[str]

    impacted_regions: list[str]

    impacted_customers: int

    severity: str