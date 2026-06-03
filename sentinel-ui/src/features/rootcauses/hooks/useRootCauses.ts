import { useQuery } from "@tanstack/react-query";

import {
  getRootCauses,
} from "@/api/rootcauses";

export function useRootCauses() {
  return useQuery({
    queryKey: [
      "rootcauses",
    ],

    queryFn:
      getRootCauses,

    refetchInterval:
      30000,
  });
}