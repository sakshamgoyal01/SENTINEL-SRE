class EvidenceAnalyzer:

    def analyze(
        self,
        investigation_result
    ) -> list[str]:

        indicators = []

        summary = (
            investigation_result
            .summary
            .lower()
        )

        findings = " ".join(
            investigation_result.findings
        ).lower()

        evidence_text = " ".join(

            [
                evidence.description
                for evidence in
                investigation_result.evidence
            ]

        ).lower()

        content = (
            f"{summary} "
            f"{findings} "
            f"{evidence_text}"
        )

        if "timeout" in content:

            indicators.append(
                "TIMEOUT"
            )

        if "oom" in content:

            indicators.append(
                "OOM"
            )

        if (
            "crashloopbackoff"
            in content
        ):

            indicators.append(
                "APPLICATION"
            )

        if (
            "connection refused"
            in content
        ):

            indicators.append(
                "DEPENDENCY"
            )

        if "dns" in content:

            indicators.append(
                "DNS"
            )

        if (
            "deployment"
            in content
        ):

            indicators.append(
                "DEPLOYMENT"
            )

        if (
            "config"
            in content
        ):

            indicators.append(
                "CONFIG"
            )

        return indicators