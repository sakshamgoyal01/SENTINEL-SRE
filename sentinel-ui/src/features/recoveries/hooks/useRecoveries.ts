import { useQuery } from "@tanstack/react-query";

import {
  getRecoveries,
} from "@/api/recoveries";

export function useRecoveries() {
  return useQuery({
    queryKey: [
      "recoveries",
    ],

    queryFn:
      getRecoveries,

    refetchInterval:
      30000,
  });
}