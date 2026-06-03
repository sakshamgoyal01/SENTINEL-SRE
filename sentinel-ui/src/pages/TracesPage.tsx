import { useState } from "react";

import {
  useTraces,
} from "@/features/traces/hooks/useTraces";

import {
  TraceFilters,
} from "@/features/traces/components/TraceFilters";

import {
  TraceStats,
} from "@/features/traces/components/TraceStats";

import {
  TraceLatencyChart,
} from "@/features/traces/components/TraceLatencyChart";

import {
  TraceCards,
} from "@/features/traces/components/TraceCards";

import {
  TraceTable,
} from "@/features/traces/components/TraceTable";

import {
  TraceDrawer,
} from "@/features/traces/components/TraceDrawer";

export default function TracesPage() {

  const {
    data,
    isLoading,
  } = useTraces();

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

  const traces =
    data ?? [];

  const filtered =
    traces.filter(
      (trace: any) =>
        trace.operation
          .toLowerCase()
          .includes(
            search.toLowerCase()
          )
    );

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">
        Distributed Tracing Center
      </h1>

      <TraceFilters
        search={search}
        setSearch={setSearch}
      />

      <TraceStats
        traces={filtered}
      />

      <TraceLatencyChart
        traces={filtered}
      />

      <TraceCards
        traces={filtered}
        onSelect={setSelected}
      />

      <TraceTable
        traces={filtered}
        onSelect={setSelected}
      />

      <TraceDrawer
        trace={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}