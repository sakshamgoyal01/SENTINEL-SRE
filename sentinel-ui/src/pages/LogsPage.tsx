import { useState } from "react";

import {
  useLogs,
} from "@/features/logs/hooks/useLogs";

import {
  LogFilters,
} from "@/features/logs/components/LogFilters";

import {
  LogStats,
} from "@/features/logs/components/LogStats";

import {
  LogCards,
} from "@/features/logs/components/LogCards";

import {
  LogTable,
} from "@/features/logs/components/LogTable";

import {
  LogDrawer,
} from "@/features/logs/components/LogDrawer";

export default function LogsPage() {

  const {
    data,
    isLoading,
  } = useLogs();

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

  const logs =
    data ?? [];

  const filtered =
    logs.filter(
      (log: any) =>
        log.message
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
        Logs Center
      </h1>

      <LogFilters
        search={search}
        setSearch={setSearch}
      />

      <LogStats
        logs={filtered}
      />

      <LogCards
        logs={filtered}
        onSelect={
          setSelected
        }
      />

      <LogTable
        logs={filtered}
        onSelect={
          setSelected
        }
      />

      <LogDrawer
        log={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}