# test_execution_publish.py

from datetime import datetime

from ai.models.approval_action import (
    ApprovalAction
)

from ai.models.approval_decision import (
    ApprovalDecision
)

from ai.publishers.approval_publisher import (
    ApprovalPublisher
)

decision = ApprovalDecision(

    approval_id="manual-test",

    service="payment-service",

    approved=True,

    requires_human_approval=False,

    reason="manual test",

    actions=[

        ApprovalAction(

            action_type="RESTART_POD",

            priority="HIGH",

            automated=True
        )
    ],

    generated_at=datetime.utcnow()
)

ApprovalPublisher().publish(
    decision
)
