export interface Incident {
  id: string;

  service: string;

  incident_priority: string;

  impact_score: number;

  final_risk_score: number;

  escalation_required: boolean;

  requires_human_review: boolean;

  created_at: string;

  aggregated_event: {
    summary: string;
    category: string;
    severity: string;
    count: number;
  };
}