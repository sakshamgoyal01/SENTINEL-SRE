import { useState } from "react";

import {
  useRootCauses,
} from "@/features/rootcauses/hooks/useRootCauses";

import {
  RootCauseFilters,
} from "@/features/rootcauses/components/RootCauseFilters";

import {
  RootCauseStats,
} from "@/features/rootcauses/components/RootCauseStats";

import {
  RootCauseCards,
} from "@/features/rootcauses/components/RootCauseCards";

import {
  RootCauseTable,
} from "@/features/rootcauses/components/RootCauseTable";

import {
  RootCauseDrawer,
} from "@/features/rootcauses/components/RootCauseDrawer";

export default function RootCausesPage() {
  const {
    data,
    isLoading,
  } = useRootCauses();

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

  const rootCauses =
    data ?? [];

  const filtered =
    rootCauses.filter(
      (rootCause: any) =>
        rootCause.service
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
        <h2
          className="
          text-2xl
          font-bold
          "
        >
          No Root Causes Found
        </h2>

        <p
          className="
          text-muted-foreground
          "
        >
          No matching root causes.
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
      <h1
        className="
        text-3xl
        font-bold
        "
      >
        Root Cause Explorer
      </h1>

      <RootCauseFilters
        search={search}
        setSearch={setSearch}
      />

      <RootCauseStats
        rootCauses={filtered}
      />

      <RootCauseCards
        rootCauses={filtered}
        onSelect={
          setSelected
        }
      />

      <RootCauseTable
        rootCauses={filtered}
        onSelect={
          setSelected
        }
      />

      <RootCauseDrawer
        rootCause={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}