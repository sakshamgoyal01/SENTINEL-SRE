from processing.models.aggregated_event import (
    AggregatedEvent
)

from processing.models.aggregation_result import (
    AggregationResult
)

from processing.aggregation.aggregation_window import (
    AggregationWindow
)


class LogAggregator:

    THRESHOLD = 20

    def __init__(self):

        self.windows = {}

    def aggregate(
        self,
        event
    ) -> AggregationResult:

        key = (
            f"{event.service}:"
            f"{event.category}"
        )

        if key not in self.windows:

            self.windows[key] = (
                AggregationWindow()
            )

        window = self.windows[key]

        window.add(event)

        if (
            window.size()
            < self.THRESHOLD
        ):
            return AggregationResult()

        events = window.events()

        aggregated = AggregatedEvent(

            aggregation_key=key,

            category=event.category,

            severity=event.severity,

            count=len(events),

            first_seen=(
                events[0].timestamp
            ),

            last_seen=(
                events[-1].timestamp
            ),

            services=[
                event.service
            ],

            summary=(
                f"{len(events)} "
                f"{event.category} "
                f"events detected"
            ),

            risk_score=max(
                e.risk_score
                for e in events
            ),

            source_events=len(
                events
            )
        )

        return AggregationResult(

            triggered=True,

            aggregated_event=aggregated
        )