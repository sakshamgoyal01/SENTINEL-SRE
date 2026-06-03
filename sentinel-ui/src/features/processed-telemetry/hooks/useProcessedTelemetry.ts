import { useQuery } from "@tanstack/react-query";

import {
  getProcessedTelemetry,
} from "@/api/processedTelemetry";

export function useProcessedTelemetry() {
  return useQuery({
    queryKey: [
      "processed-telemetry",
    ],

    queryFn:
      getProcessedTelemetry,

    refetchInterval:
      10000,
  });
}
