import { useState } from "react";

import {
  useAggregatedEvents,
} from "@/features/aggregated-events/hooks/useAggregatedEvents";

import {
  AggregatedEventFilters,
} from "@/features/aggregated-events/components/AggregatedEventFilters";

import {
  AggregatedEventStats,
} from "@/features/aggregated-events/components/AggregatedEventStats";

import {
  AggregatedEventCards,
} from "@/features/aggregated-events/components/AggregatedEventCards";

import {
  AggregatedEventTable,
} from "@/features/aggregated-events/components/AggregatedEventTable";

import {
  AggregatedEventDrawer,
} from "@/features/aggregated-events/components/AggregatedEventDrawer";

export default function AggregatedEventsPage() {

  const {
    data,
    isLoading,
  } =
    useAggregatedEvents();

  const [
    search,
    setSearch,
  ] =
    useState("");

  const [
    selected,
    setSelected,
  ] =
    useState<any>(
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

  const events =
    data ?? [];

  const filtered =
    events.filter(
      (
        event: any
      ) =>
        event.summary
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
        Aggregated Events Center
      </h1>

      <AggregatedEventFilters
        search={search}
        setSearch={setSearch}
      />

      <AggregatedEventStats
        events={filtered}
      />

      <AggregatedEventCards
        events={filtered}
        onSelect={
          setSelected
        }
      />

      <AggregatedEventTable
        events={filtered}
        onSelect={
          setSelected
        }
      />

      <AggregatedEventDrawer
        event={selected}
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
