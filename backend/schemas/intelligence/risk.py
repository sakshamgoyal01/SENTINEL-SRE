from pydantic import BaseModel


class CreateRiskRequest(
    BaseModel
):

    risk_id: str

    rootcause_id: str

    service: str

    priority: str

    blast_radius: dict

    impact_assessment: dict

    risk_summary: dict


class UpdateRiskRequest(
    BaseModel
):

    priority: str | None = None

    blast_radius: dict | None = None

    impact_assessment: dict | None = None

    risk_summary: dict | None = None


class RiskResponse(
    BaseModel
):

    id: str

    risk_id: str

    rootcause_id: str

    service: str

    priority: str

    blast_radius: dict

    impact_assessment: dict

    risk_summary: dict

    model_config = {
        "from_attributes": True
    }