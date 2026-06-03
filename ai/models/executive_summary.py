from pydantic import BaseModel


class ExecutiveSummary(BaseModel):

    incident_summary: str

    root_cause_summary: str

    impact_summary: str

    remediation_summary: str