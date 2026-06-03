export interface DLQEntry {
  id: string;

  dlq_id: string;

  source_topic: string;

  error_message: string;

  failed_at: string | null;

  payload: {
    service?: string;
  };

  created_at: string;
}
