from ingestion.normalization.deduplicator import (
    is_duplicate
)


def test_duplicate_detection():

    event = {
        "event_id": "abc123"
    }

    assert is_duplicate(event) is False
    assert is_duplicate(event) is True