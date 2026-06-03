import { useState } from "react";

import {
  useProcessedTelemetry,
} from "@/features/processed-telemetry/hooks/useProcessedTelemetry";

import {
  ProcessedTelemetryFilters,
} from "@/features/processed-telemetry/components/ProcessedTelemetryFilters";

import {
  ProcessedTelemetryStats,
} from "@/features/processed-telemetry/components/ProcessedTelemetryStats";

import {
  ProcessedTelemetryCards,
} from "@/features/processed-telemetry/components/ProcessedTelemetryCards";

import {
  ProcessedTelemetryTable,
} from "@/features/processed-telemetry/components/ProcessedTelemetryTable";

import {
  ProcessedTelemetryDrawer,
} from "@/features/processed-telemetry/components/ProcessedTelemetryDrawer";

export default function ProcessedTelemetryPage() {

  const {
    data,
    isLoading,
  } =
    useProcessedTelemetry();

  const [
    search,
    setSearch,
  ] = useState("");

  const [
    selected,
    setSelected,
  ] = useState<any>(
    null
  );

  if (
    isLoading
  ) {
    return (
      <div>
        Loading...
      </div>
    );
  }

  const telemetry =
    data ?? [];

  const filtered =
    telemetry.filter(
      (item: any) =>
        item.service
          .toLowerCase()
          .includes(
            search.toLowerCase()
          )
    );

  return (
    <div
      className="
      space-y-6
      "
    >
      <h1
        className="
        text-3xl
        font-bold
        "
      >
        Processed Telemetry
      </h1>

      <ProcessedTelemetryFilters
        search={search}
        setSearch={setSearch}
      />

      <ProcessedTelemetryStats
        telemetry={filtered}
      />

      <ProcessedTelemetryCards
        telemetry={filtered}
        onSelect={
          setSelected
        }
      />

      <ProcessedTelemetryTable
        telemetry={filtered}
        onSelect={
          setSelected
        }
      />

      <ProcessedTelemetryDrawer
        telemetry={selected}
        open={
          !!selected
        }
        onOpenChange={() =>
          setSelected(
            null
          )
        }
      />
    </div>
  );
}
