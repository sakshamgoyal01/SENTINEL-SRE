from ingestion.normalization.timestamp_normalizer import (
    normalize_timestamp
)


def test_timestamp_normalization():

    normalized = normalize_timestamp(
        "2026-05-28T10:00:00"
    )

    assert normalized.endswith("+00:00")


def test_unix_timestamp():

    normalized = normalize_timestamp(
        1748426400
    )

    assert "+00:00" in normalized