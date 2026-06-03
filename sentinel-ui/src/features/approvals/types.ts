export interface ApprovalAction {
  action_type: string;
}

export interface Approval {
  id: string;

  approval_id: string;

  service: string;

  reason: string;

  approved: boolean;

  requires_human_approval: boolean;

  generated_at: string;

  created_at: string;

  updated_at: string;

  actions: ApprovalAction[];
}