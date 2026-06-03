import { useQuery } from "@tanstack/react-query";

import {
  getAggregatedEvents,
} from "@/api/aggregatedEvents";

export function useAggregatedEvents() {
  return useQuery({
    queryKey: [
      "aggregated-events",
    ],

    queryFn:
      getAggregatedEvents,

    refetchInterval:
      10000,
  });
}
