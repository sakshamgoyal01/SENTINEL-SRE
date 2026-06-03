export interface AggregatedEvent {
  id: string;

  aggregation_key: string;

  category: string;

  summary: string;

  severity: string;

  count: number;

  services: string[];

  created_at: string;
}
