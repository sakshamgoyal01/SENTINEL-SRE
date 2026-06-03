from pydantic import BaseModel


class Metadata(BaseModel):

    cluster: str

    namespace: str

    node: str | None = None

    pod: str | None = None

    container: str | None = None

    environment: str

    team: str | None = None

    region: str | None = None