from ai.state.state_engine import (
    StateEngine
)


def test_state_engine():

    result = (

        StateEngine()
        .process(

            incident_id="inc-1",

            service=
            "payment-service",

            topic=
            "sentinel.execution.results"
        )
    )

    assert (
        result.current_state
        ==
        "EXECUTING"
    )

    assert (
        result.service
        ==
        "payment-service"
    )