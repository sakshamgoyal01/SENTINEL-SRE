class SeverityClassifier:

    VALID_LEVELS = {

        "INFO",

        "WARNING",

        "ERROR",

        "CRITICAL"
    }

    def classify(
        self,
        severity: str
    ) -> str:

        if severity in self.VALID_LEVELS:

            return severity

        return "INFO"