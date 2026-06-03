import { useQuery } from "@tanstack/react-query";

import {
  getRemediations,
} from "@/api/remediations";

export function useRemediations() {
  return useQuery({
    queryKey: [
      "remediations",
    ],

    queryFn:
      getRemediations,

    refetchInterval:
      30000,
  });
}