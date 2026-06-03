export interface Recovery {
  id: string;

  recovery_id: string;

  verification_id: string;

  service: string;

  recovery_status: string;

  strategy: {
    type: string;
  };

  created_at: string;

  updated_at: string;
}