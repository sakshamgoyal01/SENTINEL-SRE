from pydantic import BaseModel


class VerificationCheck(
    BaseModel
):

    check_type: str

    passed: bool

    details: str