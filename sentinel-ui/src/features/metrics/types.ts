export interface Metric {
  id: string;

  event_id: string;

  metric_name: string;

  service: string;

  value: number;

  unit: string;

  source: string;

  cluster: string;

  namespace: string;

  timestamp: string;

  labels: {
    pod: string;
  };
}