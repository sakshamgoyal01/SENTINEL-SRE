import asyncio
from datetime import datetime, UTC
import uuid
from backend.database.session import (
    SessionLocal
)

from backend.core.container import (
    Container
)

from backend.persistence.event_persistence_manager import (
    EventPersistenceManager
)


TEST_EVENTS = {

    "sentinel.incidents": {
        "service": "payment-service",
        "incident_priority": "P1",
        "impact_score": 90.0,
        "final_risk_score": 95.0,
        "requires_human_review": True,
        "escalation_required": True,
        "aggregated_event": {
            "aggregation_key": "payment",
            "category": "availability",
            "severity": "CRITICAL",
            "count": 100,
            "services": [
                "payment-service"
            ],
            "summary": "Timeout burst"
        }
    },

    "sentinel.investigation.results": {
        "investigation_id": str(
            uuid.uuid4()
        ),
        "incident_id": "incident-test",
        "service": "payment-service",
        "severity": "CRITICAL",
        "priority": "P1",
        "findings": {
            "summary": "Dependency failure"
        },
        "evidence": [
            "Database timeout"
        ],
        "confidence": 0.95
    },

    "sentinel.rootcause.results": {
        "rootcause_id": str(
            uuid.uuid4()
        ),
        "investigation_id": "investigation-test",
        "service": "payment-service",
        "severity": "CRITICAL",
        "priority": "P1",
        "root_cause": {
            "cause_type": "DATABASE_FAILURE"
        },
        "causal_chain": {
            "trigger": "DB Timeout"
        },
        "evidence": [
            "Connection refused"
        ],
        "confidence": 0.96
    },

    "sentinel.risk.results": {
        "risk_id": str(
            uuid.uuid4()
        ),
        "rootcause_id": "rootcause-test",
        "service": "payment-service",
        "priority": "P1",
        "blast_radius": {
            "impacted_services": [
                "checkout-service"
            ]
        },
        "impact_assessment": {
            "customer_impact": "HIGH"
        },
        "risk_summary": {
            "risk_level": "CRITICAL"
        }
    },

    "sentinel.remediation.results": {
        "remediation_id": str(
            uuid.uuid4()
        ),
        "risk_id": "risk-test",
        "service": "payment-service",
        "priority": "P1",
        "plan": {
            "runbook": "RUNBOOK"
        }
    },

    "sentinel.knowledge.records": {
        "knowledge_id": str(
            uuid.uuid4()
        ),
        "service": "payment-service",
        "pattern": {
            "incident_type":
                "SERVICE_DEPENDENCY"
        },
        "remediation": {
            "successful": True
        },
        "created_at_event": datetime.now(UTC)
    },

    "sentinel.executive.summaries": {
        "report_id": str(
            uuid.uuid4()
        ),
        "service": "payment-service",
        "generated_at": datetime.now(UTC),
        "summary": {
            "incident_summary":
                "summary"
        }
    },

    "sentinel.approved.actions": {
        "approval_id": str(
            uuid.uuid4()
        ),
        "service": "payment-service",
        "approved": True,
        "requires_human_approval": False,
        "reason": "test",
         "generated_at": datetime.now(UTC),
        "actions": [
            {
                "action_type":
                    "RESTART_POD"
            }
        ]
    },

    "sentinel.execution.results": {
        "execution_id": str(
            uuid.uuid4()
        ),
        "approval_id": "approval-test",
        "service": "payment-service",
        "executed": True,
        "status": "SUCCESS",
        "mode": "DRY_RUN",
        "actions": [
            {
                "action_type":
                    "RESTART_POD"
            }
        ]
    },

    "sentinel.verification.results": {
        "verification_id": str(
            uuid.uuid4()
        ),
        "execution_id": "execution-test",
        "service": "payment-service",
        "verified": True,
        "health_status": "HEALTHY",
        "verification_result": "SUCCESS",
        "checks": [
            {
                "check": "health"
            }
        ]
    },

    "sentinel.recovery.results": {
        "recovery_id": str(
            uuid.uuid4()
        ),
        "verification_id":
            "verification-test",
        "service": "payment-service",
        "recovery_status":
            "NOT_REQUIRED",
        "strategy": {
            "type": "NO_ACTION"
        }
    },

    "sentinel.escalations": {
        "escalation_id": str(
            uuid.uuid4()
        ),
        "recovery_id":
            "recovery-test",
        "service":
            "payment-service",
        "escalation_reason":
            "Recovery failed",
        "target": {
            "team": "SRE"
        }
    },

    "sentinel.execution.audit": {
        "audit_id": str(
            uuid.uuid4()
        ),
        "service":
            "payment-service",
        "approval_id": None,
        "execution_id": None,
        "verification_id": None,
        "recovery_id": None,
        "status": "SUCCESS",
        "details": "Audit record"
    },

    "sentinel.incident.state": {
        "incident_id":
            "incident-test",
        "service":
            "payment-service",
        "current_state":
            "VERIFYING",
        "source_topic":
            "sentinel.verification.results",
         "updated_at_event": datetime.now(UTC)
    }
}


async def main():

    async with SessionLocal() as session:

        container = Container(
            session
        )

        manager = (
            EventPersistenceManager
            .from_registry(
                container.get_handler_instances()
            )
        )

        print()
        print(
            "=" * 60
        )
        print(
            "TESTING ALL SENTINEL TOPICS"
        )
        print(
            "=" * 60
        )

        passed = 0
        failed = 0

        for (
            topic,
            payload
        ) in TEST_EVENTS.items():

            try:

                await manager.persist_event(
                    topic=topic,
                    payload=payload,
                )

                await session.commit()

                passed += 1

                print(
                    f"[PASS] {topic}"
                )

            except Exception as exc:

                await session.rollback()

                failed += 1

                print(
                    f"[FAIL] {topic}"
                )

                print(
                    f"Reason: {exc}"
                )

        print()
        print(
            "=" * 60
        )
        print(
            f"PASSED : {passed}"
        )
        print(
            f"FAILED : {failed}"
        )
        print(
            "=" * 60
        )

        if failed == 0:

            print()
            print(
                "ALL TOPICS VALIDATED SUCCESSFULLY"
            )

        else:

            print()
            print(
                "SOME TOPICS FAILED VALIDATION"
            )


if __name__ == "__main__":

    asyncio.run(
        main()
    )