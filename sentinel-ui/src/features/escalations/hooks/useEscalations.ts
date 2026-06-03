import { useQuery } from "@tanstack/react-query";

import {
  getEscalations,
} from "@/api/escalations";

export function useEscalations() {
  return useQuery({
    queryKey: [
      "escalations",
    ],

    queryFn:
      getEscalations,

    refetchInterval:
      10000,
  });
}