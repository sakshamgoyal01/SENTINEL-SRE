from processing.routing.routing_rules import (
    ROUTING_RULES
)


class DestinationRouter:

    def get_destinations(
        self,
        priority: str
    ) -> list[str]:

        return ROUTING_RULES.get(
            priority,
            ["audit"]
        )