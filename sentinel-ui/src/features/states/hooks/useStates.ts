import { useQuery } from "@tanstack/react-query";

import {
  getStates,
} from "@/api/states";

export function useStates() {
  return useQuery({
    queryKey: [
      "states",
    ],

    queryFn:
      getStates,

    refetchInterval:
      10000,
  });
}
