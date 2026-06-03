from ai.state.state_mapper import (
    StateMapper
)

from ai.state.state_manager import (
    StateManager
)


class StateAgent:

    def __init__(self):

        self.mapper = (
            StateMapper()
        )

        self.manager = (
            StateManager()
        )

    def process(

        self,

        incident_id,

        service,

        topic
    ):

        state = (

            self.mapper
            .map_state(
                topic
            )
        )

        return (

            self.manager
            .update(

                incident_id,

                service,

                state,

                topic
            )
        )