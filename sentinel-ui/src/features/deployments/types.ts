export interface Deployment {
  id: string;

  deployment_name: string;

  image: string;

  namespace: string;

  replicas: number;

  available_replicas: number;

  updated_replicas: number;

  strategy: string;

  timestamp: string;
}