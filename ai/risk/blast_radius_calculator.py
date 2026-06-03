from ai.models.blast_radius import (
    BlastRadius
)


class BlastRadiusCalculator:

    def calculate(
        self,
        rootcause_result
    ) -> BlastRadius:

        priority = (
            rootcause_result
            .priority
        )

        if priority == "P1":

            services = [

                rootcause_result.service,

                "checkout-service",

                "order-service",

                "inventory-service",

                "notification-service"
            ]

            customers = 10000

        elif priority == "P2":

            services = [

                rootcause_result.service,

                "checkout-service",

                "order-service"
            ]

            customers = 3000

        else:

            services = [
                rootcause_result.service
            ]

            customers = 500

        return BlastRadius(

            impacted_services=services,

            impacted_regions=[
                "us-east-1"
            ],

            impacted_customers=customers,

            severity=(
                rootcause_result
                .severity
            )
        )