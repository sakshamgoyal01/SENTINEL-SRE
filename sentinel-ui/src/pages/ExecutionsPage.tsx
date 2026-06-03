import { useState } from "react";

import {
  useExecutions,
} from "@/features/executions/hooks/useExecutions";

import {
  ExecutionFilters,
} from "@/features/executions/components/ExecutionFilters";

import {
  ExecutionStats,
} from "@/features/executions/components/ExecutionStats";

import {
  ExecutionCards,
} from "@/features/executions/components/ExecutionCards";

import {
  ExecutionTable,
} from "@/features/executions/components/ExecutionTable";

import {
  ExecutionDrawer,
} from "@/features/executions/components/ExecutionDrawer";

export default function ExecutionsPage() {

  const {
    data,
    isLoading,
  } = useExecutions();

  const [
    search,
    setSearch,
  ] = useState("");

  const [
    selected,
    setSelected,
  ] = useState<any>(null);

  if (isLoading) {
    return (
      <div>
        Loading...
      </div>
    );
  }

  const executions =
    data ?? [];

  const filtered =
    executions.filter(
      (execution: any) =>
        execution.service
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
        Execution Center
      </h1>

      <ExecutionFilters
        search={search}
        setSearch={setSearch}
      />

      <ExecutionStats
        executions={filtered}
      />

      <ExecutionCards
        executions={filtered}
        onSelect={
          setSelected
        }
      />

      <ExecutionTable
        executions={filtered}
        onSelect={
          setSelected
        }
      />

      <ExecutionDrawer
        execution={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}