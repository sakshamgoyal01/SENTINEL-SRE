from backend.api.read_only_router import (
    ReadOnlyRouter
)


def test_import():

    router = ReadOnlyRouter

    assert (
        router
        is not None
    )

    print(
        "PASS"
    )


if __name__ == "__main__":

    test_import()