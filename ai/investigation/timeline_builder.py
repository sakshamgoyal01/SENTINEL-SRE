from ai.models.timeline_event import (
    TimelineEvent
)


class TimelineBuilder:

    def build(
        self,
        prioritized_event
    ) -> list[TimelineEvent]:

        event = (
            prioritized_event
            .aggregated_event
        )

        return [

            TimelineEvent(
                timestamp=event.first_seen,
                event_type="incident_start",
                description=(
                    "Incident signals detected"
                )
            ),

            TimelineEvent(
                timestamp=event.last_seen,
                event_type="incident_end",
                description=(
                    "Latest observed signal"
                )
            )
        ]