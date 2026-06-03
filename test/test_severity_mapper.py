from ingestion.normalization.severity_mapper import (
    normalize_severity
)


def test_error_mapping():

    result = normalize_severity(
        "ERR"
    )

    assert result == "ERROR"


def test_warning_mapping():

    result = normalize_severity(
        "WARN"
    )

    assert result == "WARNING"


def test_default_mapping():

    result = normalize_severity(
        "something-random"
    )

    assert result == "INFO"