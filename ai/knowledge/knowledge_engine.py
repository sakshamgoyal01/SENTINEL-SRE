from ai.knowledge.knowledge_agent import (
    KnowledgeAgent
)


class KnowledgeEngine:

    def __init__(self):

        self.agent = (
            KnowledgeAgent()
        )

    def process(
        self,
        remediation_result
    ):

        return (
            self.agent
            .analyze(
                remediation_result
            )
        )