export interface Audit {
  id: string;

  audit_id: string;

  service: string;

  status: string;

  details: string;

  approval_id?: string | null;

  execution_id?: string | null;

  verification_id?: string | null;

  recovery_id?: string | null;

  created_at: string;
}