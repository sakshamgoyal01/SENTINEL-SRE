from enum import StrEnum


class Severity(StrEnum):

    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class Priority(StrEnum):

    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    P4 = "P4"