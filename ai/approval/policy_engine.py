class PolicyEngine:

    DENY_ACTIONS = {

        "DELETE_RESOURCE"
    }

    HUMAN_ACTIONS = {

        "ROLLBACK_PRODUCTION"
    }

    AUTO_ACTIONS = {

        "RESTART_POD",

        "SCALE_DEPLOYMENT"
    }

    def evaluate(
        self,
        action_type: str
    ) -> str:

        if (
            action_type
            in self.DENY_ACTIONS
        ):

            return "DENY"

        if (
            action_type
            in self.HUMAN_ACTIONS
        ):

            return "HUMAN"

        if (
            action_type
            in self.AUTO_ACTIONS
        ):

            return "AUTO"

        return "HUMAN"