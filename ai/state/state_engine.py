from ai.state.state_agent import (
    StateAgent
)


class StateEngine:

    def __init__(self):

        self.agent = (
            StateAgent()
        )

    def process(

        self,

        incident_id,

        service,

        topic
    ):

        return (

            self.agent
            .process(

                incident_id,

                service,

                topic
            )
        )