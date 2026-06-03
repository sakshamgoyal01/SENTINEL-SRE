class ActionMapper:

    def map_action(
        self,
        approval_action,
        service: str
    ):

        mapping = {

            "ENABLE_CIRCUIT_BREAKER":
                "SERVICE_MESH",

            "CHECK_HEALTH":
                service,

            "VERIFY_DEPENDENCY":
                service,

            "ESCALATE_TEAM":
                service,

            "RESTART_POD":
                service,

            "SCALE_DEPLOYMENT":
                service
        }

        return mapping.get(

            approval_action.action_type,

            service
        )