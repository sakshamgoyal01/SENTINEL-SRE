export interface Knowledge {
  id: string;

  knowledge_id: string;

  service: string;

  pattern: {
    incident_type: string;
  };

  remediation: {
    successful: boolean;
  };

  success_rate: number | null;

  created_at: string;
}
