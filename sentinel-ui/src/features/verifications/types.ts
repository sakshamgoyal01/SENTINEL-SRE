export interface Verification {
  id: string;

  verification_id: string;

  execution_id: string;

  service: string;

  verified: boolean;

  health_status: string;

  verification_result: string;

  checks: {
    check: string;
  }[];

  created_at: string;
}