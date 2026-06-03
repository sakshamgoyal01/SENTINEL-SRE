import { useQuery } from "@tanstack/react-query";

import {
  getDLQ,
} from "@/api/dlq";

export function useDLQ() {
  return useQuery({
    queryKey: [
      "dlq",
    ],

    queryFn:
      getDLQ,

    refetchInterval:
      10000,
  });
}
