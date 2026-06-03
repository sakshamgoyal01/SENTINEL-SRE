from datetime import datetime

from pydantic import BaseModel


class TimelineEvent(BaseModel):

    timestamp: datetime

    event_type: str

    description: str