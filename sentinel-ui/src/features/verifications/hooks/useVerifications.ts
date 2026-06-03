import { useQuery } from "@tanstack/react-query";

import {
  getVerifications,
} from "@/api/verifications";

export function useVerifications() {
  return useQuery({
    queryKey: [
      "verifications",
    ],

    queryFn:
      getVerifications,

    refetchInterval:
      10000,
  });
}