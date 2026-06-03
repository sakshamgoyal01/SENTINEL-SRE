from datetime import datetime

from pydantic import BaseModel

from ai.models.executive_summary import (
    ExecutiveSummary
)


class ExecutiveReport(BaseModel):

    report_id: str

    service: str

    summary: ExecutiveSummary

    generated_at: datetime