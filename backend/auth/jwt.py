from datetime import (
    datetime,
    timedelta,
    UTC
)

from jose import jwt
from jose import JWTError

SECRET_KEY = (
    "CHANGE_ME_IN_ENV"
)

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(
    subject: str,
    email: str,
    roles: list[str],
) -> str:

    expire = (
        datetime.now(UTC)
        + timedelta(
            minutes=
            ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload = {
        "sub": subject,
        "email": email,
        "roles": roles,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def decode_access_token(
    token: str,
) -> dict:

    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[
            ALGORITHM
        ],
    )


def verify_token(
    token: str,
) -> dict | None:

    try:

        return decode_access_token(
            token
        )

    except JWTError:

        return None