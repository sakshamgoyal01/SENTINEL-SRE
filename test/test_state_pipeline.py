from ai.state.state_engine import (
    StateEngine
)


def test_state_pipeline():

    result = (

        StateEngine()
        .process(

            incident_id=
            "incident-1",

            service=
            "payment-service",

            topic=
            "sentinel.verification.results"
        )
    )

    assert (
        result.current_state
        ==
        "VERIFYING"
    )

    assert (
        result.service
        ==
        "payment-service"
    )

    assert (
        result.source_topic
        ==
        "sentinel.verification.results"
    )