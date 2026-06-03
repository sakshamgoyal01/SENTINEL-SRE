export interface Risk {
  id: string;

  risk_id: string;

  rootcause_id: string;

  service: string;

  priority: string;

  risk_summary: {
    risk_level: string;
  };

  impact_assessment: {
    customer_impact: string;
  };

  blast_radius: {
    impacted_services?: string[];
    services?: string[];
  };

  created_at: string;
}