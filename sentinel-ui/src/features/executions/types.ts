export interface ExecutionAction {
  action_type: string;
}

export interface Execution {
  id: string;

  execution_id: string;

  approval_id: string;

  service: string;

  executed: boolean;

  status: string;

  mode: string;

  actions: ExecutionAction[];

  created_at: string;

  updated_at: string;
}