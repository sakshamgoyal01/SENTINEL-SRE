export interface RootCause {
  id: string;

  rootcause_id: string;

  investigation_id: string;

  service: string;

  severity: string;

  priority: string;

  confidence: number;

  evidence: string[];

  root_cause: {
    cause_type: string;
  };

  causal_chain: {
    trigger: string;
  };

  created_at: string;
}