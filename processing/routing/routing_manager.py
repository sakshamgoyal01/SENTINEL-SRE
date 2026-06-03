from processing.models.routing_result import (
    RoutingResult
)

from processing.routing.destination_router import (
    DestinationRouter
)

from processing.publishers.incident_publisher import (
    IncidentPublisher
)

from processing.publishers.alert_publisher import (
    AlertPublisher
)

from processing.publishers.audit_publisher import (
    AuditPublisher
)


class RoutingManager:

    def __init__(self):

        self.destination_router = (
            DestinationRouter()
        )

        self.incident_publisher = (
            IncidentPublisher()
        )

        self.alert_publisher = (
            AlertPublisher()
        )

        self.audit_publisher = (
            AuditPublisher()
        )

    def route(
        self,
        prioritized_event
    ) -> RoutingResult:

        destinations = (

            self.destination_router
            .get_destinations(
                prioritized_event
                .incident_priority
            )
        )

        for destination in destinations:

            if destination == "incident":

                self.incident_publisher.publish(
                    prioritized_event
                )

            elif destination == "alert":

                self.alert_publisher.publish(
                    prioritized_event
                )

            elif destination == "audit":

                self.audit_publisher.publish(
                    prioritized_event
                )

        return RoutingResult(

            routed=True,

            destinations=destinations
        )