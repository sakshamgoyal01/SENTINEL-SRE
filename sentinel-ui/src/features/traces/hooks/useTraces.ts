import { useQuery } from "@tanstack/react-query";

import {
  getTraces,
} from "@/api/traces";

export function useTraces() {
  return useQuery({
    queryKey: [
      "traces",
    ],

    queryFn:
      getTraces,

    refetchInterval:
      10000,
  });
}