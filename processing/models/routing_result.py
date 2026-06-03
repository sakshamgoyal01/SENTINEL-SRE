from pydantic import BaseModel


class RoutingResult(BaseModel):

    routed: bool

    destinations: list[str]

    errors: list[str] = []