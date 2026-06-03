from typing import List, Optional

from pydantic import BaseModel


class OperationalContext(BaseModel):

    service_type: Optional[str] = None

    dependencies: List[str] = []

    environment: str

    cluster: str

    namespace: str

    deployment_name: Optional[str] = None

    resource_type: Optional[str] = None

    infrastructure_component: Optional[str] = None

    team: Optional[str] = None

    region: Optional[str] = None

    correlated: bool = False