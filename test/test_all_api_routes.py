import sys

from fastapi.testclient import (
    TestClient
)

from backend.main import (
    app
)

client = TestClient(
    app
)


ROUTES = [

    # Health
    "/health",

    # Telemetry
    "/api/v1/metrics",
    "/api/v1/logs",
    "/api/v1/traces",
    "/api/v1/kubernetes",
    "/api/v1/deployments",
    "/api/v1/processed-telemetry",

    # Intelligence
    "/api/v1/incidents",
    "/api/v1/investigations",
    "/api/v1/rootcauses",
    "/api/v1/risks",
    "/api/v1/remediations",
    "/api/v1/knowledge",
    "/api/v1/reports",
    "/api/v1/aggregated-events",
    "/api/v1/alerts",

    # Operations
    "/api/v1/approvals",
    "/api/v1/executions",
    "/api/v1/verifications",
    "/api/v1/recoveries",
    "/api/v1/escalations",
    "/api/v1/states",
    "/api/v1/audits",

    # Platform
    "/api/v1/dlq",
]


def test_route(
    route: str,
) -> bool:

    try:

        response = client.get(
            route
        )

        if response.status_code in (
            200,
            401,
            403,
        ):

            print(
                f"[PASS] {route}"
            )

            return True

        print(
            f"[FAIL] {route}"
        )

        print(
            f"Status: "
            f"{response.status_code}"
        )

        return False

    except Exception as e:

        print(
            f"[FAIL] {route}"
        )

        print(
            f"Reason: {e}"
        )

        return False


def main():

    passed = 0
    failed = 0

    print()
    print(
        "=" * 60
    )
    print(
        "TESTING ALL API ROUTES"
    )
    print(
        "=" * 60
    )

    for route in ROUTES:

        if test_route(
            route
        ):
            passed += 1
        else:
            failed += 1

    print()
    print(
        "=" * 60
    )
    print(
        f"PASSED : {passed}"
    )
    print(
        f"FAILED : {failed}"
    )
    print(
        "=" * 60
    )

    if failed > 0:

        print()
        print(
            "SOME ROUTES FAILED"
        )

        sys.exit(1)

    print()
    print(
        "ALL API ROUTES VALIDATED"
    )


if __name__ == "__main__":

    main()