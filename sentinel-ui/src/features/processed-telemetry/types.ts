export interface ProcessedTelemetry {
  id: string;

  event_id: string;

  service: string;

  event_type: string;

  category: string;

  severity: string;

  priority: string;

  summary: string;

  risk_score: number;

  raw_event: {
    metric_name?: string;
  };

  created_at: string;
}
