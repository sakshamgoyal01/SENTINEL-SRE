import { useState } from "react";

import {
  useMetrics,
} from "@/features/metrics/hooks/useMetrics";

import {
  MetricFilters,
} from "@/features/metrics/components/MetricFilters";

import {
  MetricStats,
} from "@/features/metrics/components/MetricStats";

import {
  MetricChart,
} from "@/features/metrics/components/MetricChart";

import {
  MetricCards,
} from "@/features/metrics/components/MetricCards";

import {
  MetricTable,
} from "@/features/metrics/components/MetricTable";

import {
  MetricDrawer,
} from "@/features/metrics/components/MetricDrawer";

export default function MetricsPage() {

  const {
    data,
    isLoading,
  } = useMetrics();

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

  if (isLoading) {
    return (
      <div>
        Loading...
      </div>
    );
  }

  const metrics =
    data ?? [];

  const filtered =
    metrics.filter(
      (metric: any) =>
        metric.service
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
        Metrics Center
      </h1>

      <MetricFilters
        search={search}
        setSearch={setSearch}
      />

      <MetricStats
        metrics={filtered}
      />

      <MetricChart
        metrics={filtered}
      />

      <MetricCards
        metrics={filtered}
        onSelect={
          setSelected
        }
      />

      <MetricTable
        metrics={filtered}
        onSelect={
          setSelected
        }
      />

      <MetricDrawer
        metric={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}