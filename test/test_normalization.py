from ingestion.normalization.normalizer import normalize_event


def test_normalization():

    event = {
        "timestamp": "2026-05-28T10:00:00",
        "severity": "error",
        "service": "payment-service",
        "message": "DB timeout",
        "trace_id": "abc123"
    }

    normalized = normalize_event(event)

    assert normalized["severity"] == "ERROR"
    assert normalized["service"] == "payment-service"
    assert normalized["correlated"] is True
    assert "dependencies" in normalized