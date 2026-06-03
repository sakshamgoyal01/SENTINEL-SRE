class StateMapper:

    TOPIC_STATE_MAP = {

        "sentinel.incidents":
            "OPEN",

        "sentinel.investigation.results":
            "INVESTIGATING",

        "sentinel.rootcause.results":
            "ROOT_CAUSE_IDENTIFIED",

        "sentinel.risk.results":
            "RISK_ANALYZED",

        "sentinel.remediation.results":
            "REMEDIATION_GENERATED",

        "sentinel.approved.actions":
            "APPROVED",

        "sentinel.execution.results":
            "EXECUTING",

        "sentinel.verification.results":
            "VERIFYING",

        "sentinel.recovery.results":
            "RECOVERING"
    }

    def map_state(
        self,
        topic: str
    ):

        return self.TOPIC_STATE_MAP.get(

            topic,

            "UNKNOWN"
        )