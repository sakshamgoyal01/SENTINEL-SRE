import { useQuery } from "@tanstack/react-query";

import {
  getKnowledge,
} from "@/api/knowledge";

export function useKnowledge() {
  return useQuery({
    queryKey: [
      "knowledge",
    ],

    queryFn:
      getKnowledge,

    refetchInterval:
      10000,
  });
}
