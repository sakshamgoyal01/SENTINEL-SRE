import { useQuery } from "@tanstack/react-query";

import {
  getExecutions,
} from "@/api/executions";

export function useExecutions() {
  return useQuery({
    queryKey: [
      "executions",
    ],

    queryFn:
      getExecutions,

    refetchInterval:
      30000,
  });
}