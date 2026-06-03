import {
  useQueries,
} from "@tanstack/react-query";

import {
  getAlerts,
} from "@/api/alerts";

import {
  getIncidents,
} from "@/api/incidents";

import {
  getRisks,
} from "@/api/risks";

import {
  getInvestigations,
} from "@/api/investigations";

import {
  getExecutions,
} from "@/api/executions";

import {
  getRecoveries,
} from "@/api/recoveries";

export function useDashboard() {

  const results =
    useQueries({
      queries: [
        {
          queryKey: [
            "alerts",
          ],
          queryFn:
            getAlerts,
        },

        {
          queryKey: [
            "incidents",
          ],
          queryFn:
            getIncidents,
        },

        {
          queryKey: [
            "risks",
          ],
          queryFn:
            getRisks,
        },

        {
          queryKey: [
            "investigations",
          ],
          queryFn:
            getInvestigations,
        },

        {
          queryKey: [
            "executions",
          ],
          queryFn:
            getExecutions,
        },

        {
          queryKey: [
            "recoveries",
          ],
          queryFn:
            getRecoveries,
        },
      ],
    });

  return {
    alerts:
      results[0],

    incidents:
      results[1],

    risks:
      results[2],

    investigations:
      results[3],

    executions:
      results[4],

    recoveries:
      results[5],
  };
}