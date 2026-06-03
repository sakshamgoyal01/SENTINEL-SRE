export interface Investigation {
  id: string;

  investigation_id: string;

  incident_id: string;

  service: string;

  severity: string;

  priority: string;

  confidence: number;

  evidence: string[];

  findings: {
    summary: string;
  };

  created_at: string;
}