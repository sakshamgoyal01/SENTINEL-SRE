SEVERITY_MAP = {

    "ERR": "ERROR",

    "ERROR": "ERROR",

    "CRIT": "CRITICAL",

    "CRITICAL": "CRITICAL",

    "FATAL": "CRITICAL",

    "PANIC": "CRITICAL",

    "WARN": "WARNING",

    "WARNING": "WARNING",

    "INFO": "INFO",

    "DEBUG": "DEBUG",

    "TRACE": "DEBUG"
}


def normalize_severity(level: str):

    if not level:

        return "INFO"

    return SEVERITY_MAP.get(
        level.upper(),
        "INFO"
    )