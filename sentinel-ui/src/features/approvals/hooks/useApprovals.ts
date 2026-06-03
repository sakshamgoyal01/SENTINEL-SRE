import { useQuery } from "@tanstack/react-query";

import {
  getApprovals,
} from "@/api/approvals";

export function useApprovals() {
  return useQuery({
    queryKey: [
      "approvals",
    ],

    queryFn:
      getApprovals,

    refetchInterval:
      30000,
  });
}