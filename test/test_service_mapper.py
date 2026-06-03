from ingestion.normalization.service_mapper import (
    normalize_service
)


def test_service_mapping():

    result = normalize_service(
        "payment-api"
    )

    assert result == "payment-service"


def test_unknown_service():

    result = normalize_service(
        "custom-service"
    )

    assert result == "custom-service"