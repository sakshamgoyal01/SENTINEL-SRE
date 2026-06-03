export interface Remediation {
  id: string;

  remediation_id: string;

  risk_id: string;

  service: string;

  priority: string;

  plan: {
    runbook: string;
  };

  created_at: string;
}