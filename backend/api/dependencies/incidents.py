from backend.database.session import (
    get_db
)

from backend.core.container import (
    Container
)

from fastapi import Depends


async def get_incident_service(
    session=Depends(get_db),
):

    container = Container(
        session
    )

    return (
        container.incident_service
    )