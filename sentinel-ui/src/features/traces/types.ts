export interface Trace {
  id: string;

  trace_id: string;

  span_id: string;

  parent_span_id: string | null;

  service: string;

  operation: string;

  duration_ms: number;

  status_code: number;

  timestamp: string;

  created_at: string;
}