from fastapi import Depends

from backend.database.session import (
    get_db,
)

from backend.core.container import (
    Container,
)


async def get_incident_state_service(
    session=Depends(get_db),
):

    container = Container(
        session
    )

    return (
        container.incident_state_service
    )