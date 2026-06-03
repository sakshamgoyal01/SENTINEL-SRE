import { useQuery } from "@tanstack/react-query";

import {
  getKubernetesEvents,
} from "@/api/kubernetes";

export function useKubernetes() {
  return useQuery({
    queryKey: [
      "kubernetes",
    ],

    queryFn:
      getKubernetesEvents,

    refetchInterval:
      10000,
  });
}