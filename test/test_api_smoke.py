from fastapi.testclient import (
    TestClient
)

from backend.main import (
    app
)

client = TestClient(
    app
)


def test_health():

    response = client.get(
        "/health"
    )

    assert (
        response.status_code
        == 200
    )

    print(
        "[PASS] Health"
    )


def test_incidents():

    response = client.get(
        "/api/v1/incidents"
    )

    assert (
        response.status_code
        in [200, 401, 403]
    )

    print(
        "[PASS] Incidents Route"
    )


def test_risks():

    response = client.get(
        "/api/v1/risks"
    )

    assert (
        response.status_code
        in [200, 401, 403]
    )

    print(
        "[PASS] Risks Route"
    )


def test_alerts():

    response = client.get(
        "/api/v1/alerts"
    )

    assert (
        response.status_code
        in [200, 401, 403]
    )

    print(
        "[PASS] Alerts Route"
    )


def test_approvals():

    response = client.get(
        "/api/v1/approvals"
    )

    assert (
        response.status_code
        in [200, 401, 403]
    )

    print(
        "[PASS] Approvals Route"
    )


def main():

    print()

    print(
        "=" * 60
    )

    print(
        "TESTING API ROUTES"
    )

    print(
        "=" * 60
    )

    test_health()

    test_incidents()

    test_risks()

    test_alerts()

    test_approvals()

    print()

    print(
        "=" * 60
    )

    print(
        "ALL API ROUTES VALID"
    )

    print(
        "=" * 60
    )


if __name__ == "__main__":

    main()