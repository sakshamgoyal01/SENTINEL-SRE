export interface Report {
  id: string;

  report_id: string;

  service: string;

  generated_at: string;

  summary: {
    incident_summary: string;
  };
}
