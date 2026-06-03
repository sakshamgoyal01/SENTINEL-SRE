from ingestion.normalization.topology_enricher import (
    enrich_topology
)


def test_topology_enrichment():

    event = {
        "service": "payment-service"
    }

    enriched = enrich_topology(event)

    assert "dependencies" in enriched