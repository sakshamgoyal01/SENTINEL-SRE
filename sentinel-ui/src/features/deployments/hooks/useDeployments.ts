import { useQuery } from "@tanstack/react-query";

import {
  getDeployments,
} from "@/api/deployments";

export function useDeployments() {
  return useQuery({
    queryKey: [
      "deployments",
    ],

    queryFn:
      getDeployments,

    refetchInterval:
      10000,
  });
}