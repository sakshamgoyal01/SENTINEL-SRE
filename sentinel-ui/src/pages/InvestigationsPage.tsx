import { useState } from "react";

import {
  useInvestigations,
} from "@/features/investigations/hooks/useInvestigations";

import {
  InvestigationFilters,
} from "@/features/investigations/components/InvestigationFilters";

import {
  InvestigationStats,
} from "@/features/investigations/components/InvestigationStats";

import {
  InvestigationCards,
} from "@/features/investigations/components/InvestigationCards";

import {
  InvestigationTable,
} from "@/features/investigations/components/InvestigationTable";

import {
  InvestigationDrawer,
} from "@/features/investigations/components/InvestigationDrawer";

export default function InvestigationsPage() {
  const {
    data,
    isLoading,
  } = useInvestigations();

  const [
    selected,
    setSelected,
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

  const investigations =
    data ?? [];

  const filtered =
    investigations.filter(
      (investigation: any) =>
        investigation.service
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
          No Investigations Found
        </h2>

        <p
          className="
          text-muted-foreground
          "
        >
          No matching investigations.
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
        Investigation Center
      </h1>

      <InvestigationFilters
        search={search}
        setSearch={setSearch}
      />

      <InvestigationStats
        investigations={filtered}
      />

      <InvestigationCards
        investigations={filtered}
        onSelect={setSelected}
      />

      <InvestigationTable
        investigations={filtered}
        onSelect={setSelected}
      />

      <InvestigationDrawer
        investigation={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}