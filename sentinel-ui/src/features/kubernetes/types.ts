export interface KubernetesEvent {
  id: string;

  event_type: string;

  reason: string;

  message: string;

  timestamp: string;

  involved_object: {
    kind: string;
    name: string;
  };
}