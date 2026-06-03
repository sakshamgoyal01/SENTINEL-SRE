import { useState } from "react";

import {
  useDLQ,
} from "@/features/dlq/hooks/useDLQ";

import {
  DLQFilters,
} from "@/features/dlq/components/DLQFilters";

import {
  DLQStats,
} from "@/features/dlq/components/DLQStats";

import {
  DLQCards,
} from "@/features/dlq/components/DLQCards";

import {
  DLQTable,
} from "@/features/dlq/components/DLQTable";

import {
  DLQDrawer,
} from "@/features/dlq/components/DLQDrawer";

export default function DLQPage() {

  const {
    data,
    isLoading,
  } =
    useDLQ();

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

  const entries =
    data ?? [];

  const filtered =
    entries.filter(
      (item: any) =>
        (
          item.payload
            ?.service || ""
        )
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
        Dead Letter Queue
      </h1>

      <DLQFilters
        search={search}
        setSearch={setSearch}
      />

      <DLQStats
        entries={filtered}
      />

      <DLQCards
        entries={filtered}
        onSelect={
          setSelected
        }
      />

      <DLQTable
        entries={filtered}
        onSelect={
          setSelected
        }
      />

      <DLQDrawer
        entry={selected}
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
