from datetime import datetime

from pydantic import BaseModel


class ExecutiveReportResponse(BaseModel):
    id: str
    report_id: str
    service: str
    summary: dict
    generated_at: datetime

    model_config = {
        "from_attributes": True
    }