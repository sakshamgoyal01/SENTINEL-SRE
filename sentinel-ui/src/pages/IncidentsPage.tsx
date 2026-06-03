import { useState } from "react";

import {
  useIncidents,
} from "@/features/incidents/hooks/useIncidents";

import {
  IncidentStats,
} from "@/features/incidents/components/IncidentStats";

import {
  IncidentCards,
} from "@/features/incidents/components/IncidentCards";

import {
  IncidentFilters,
} from "@/features/incidents/components/IncidentFilters";

import {
  IncidentTable,
} from "@/features/incidents/components/IncidentTable";

import {
  IncidentDrawer,
} from "@/features/incidents/components/IncidentDrawer";

import {
  IncidentTrendChart,
} from "@/features/incidents/components/IncidentTrendChart";

export default function IncidentsPage() {
  const {
    data,
    isLoading,
  } = useIncidents();

  const [
    selectedIncident,
    setSelectedIncident,
  ] = useState<any>(null);

  const [
    search,
    setSearch,
  ] = useState("");

  if (isLoading) {
    return (
      <div>
        Loading...
      </div>
    );
  }

  const incidents =
    data ?? [];

  const filtered =
    incidents.filter(
      (incident: any) =>
        incident.service
          .toLowerCase()
          .includes(
            search.toLowerCase()
          )
    );

  if (filtered.length === 0) {
    return (
      <div
        className="
        flex
        flex-col
        items-center
        justify-center
        py-20
        "
      >
        <div
          className="
          text-6xl
          "
        >
          🟢
        </div>

        <h2
          className="
          mt-4
          text-2xl
          font-bold
          "
        >
          No Active Incidents
        </h2>

        <p
          className="
          text-muted-foreground
          "
        >
          System is healthy.
        </p>
      </div>
    );
  }

  return (
    <div
      className="
      space-y-6
      "
    >
      <div>
        <h1
          className="
          text-3xl
          font-bold
          "
        >
          Incident Command Center
        </h1>
      </div>

      <IncidentFilters
        search={search}
        setSearch={setSearch}
      />

      <IncidentStats
        incidents={filtered}
      />

      <IncidentTrendChart
        incidents={filtered}
      />

      <IncidentCards
        incidents={filtered}
        onSelect={
          setSelectedIncident
        }
      />

      <IncidentTable
        incidents={filtered}
        onSelect={
          setSelectedIncident
        }
      />

      <IncidentDrawer
        incident={
          selectedIncident
        }
        open={
          !!selectedIncident
        }
        onOpenChange={() =>
          setSelectedIncident(
            null
          )
        }
      />
    </div>
  );
}