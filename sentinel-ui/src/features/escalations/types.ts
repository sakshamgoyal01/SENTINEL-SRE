export interface Escalation {
  id: string;

  escalation_id: string;

  service: string;

  escalation_reason: string;

  recovery_id: string;

  target: {
    team: string;
  };

  created_at: string;
}