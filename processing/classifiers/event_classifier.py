class EventClassifier:

    FAMILY_MAP = {

        "performance":
            "performance",

        "availability":
            "reliability",

        "deployment":
            "release",

        "infrastructure":
            "infrastructure",

        "security":
            "security",

        "application":
            "application",

        "kubernetes":
            "backend"
    }

    def classify(
        self,
        category: str
    ) -> str:

        return self.FAMILY_MAP.get(
            category,
            "observability"
        )