from ingestion.normalization.trace_correlator import (
    correlate_trace
)


def test_trace_correlation():

    event = {
        "trace_id": "abc123"
    }

    correlated = correlate_trace(event)

    assert correlated["correlated"] is True