from backend.auth.password import (
    hash_password,
    verify_password,
)

from backend.auth.jwt import (
    create_access_token,
    verify_token,
)


def test_password_hashing():

    print("\nTesting Password Hashing...")

    password = "Sentinel123!"

    hashed = hash_password(
        password
    )

    assert hashed != password

    assert verify_password(
        password,
        hashed,
    )

    assert not verify_password(
        "wrong-password",
        hashed,
    )

    print("PASS")


def test_jwt():

    print("\nTesting JWT...")

    token = create_access_token(
        subject="user-123",
        email="admin@sentinel.io",
        roles=[
            "ADMIN",
            "SRE",
        ],
    )

    payload = verify_token(
        token
    )

    assert payload is not None

    assert (
        payload["sub"]
        == "user-123"
    )

    assert (
        payload["email"]
        == "admin@sentinel.io"
    )

    assert (
        "ADMIN"
        in payload["roles"]
    )

    print("PASS")


def main():

    print(
        "\n=============================="
    )

    print(
        "TESTING AUTH"
    )

    print(
        "=============================="
    )

    test_password_hashing()

    test_jwt()

    print(
        "\n=============================="
    )

    print(
        "ALL AUTH TESTS PASSED"
    )

    print(
        "=============================="
    )


if __name__ == "__main__":

    main()