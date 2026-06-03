import { useState } from "react";

import {
  useRisks,
} from "@/features/risks/hooks/useRisks";

import {
  RiskFilters,
} from "@/features/risks/components/RiskFilters";

import {
  RiskStats,
} from "@/features/risks/components/RiskStats";

import {
  RiskCards,
} from "@/features/risks/components/RiskCards";

import {
  RiskTable,
} from "@/features/risks/components/RiskTable";

import {
  RiskDrawer,
} from "@/features/risks/components/RiskDrawer";

export default function RisksPage() {
  const {
    data,
    isLoading,
  } = useRisks();

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

  const risks =
    data ?? [];

  const filtered =
    risks.filter(
      (risk: any) =>
        risk.service
          .toLowerCase()
          .includes(
            search.toLowerCase()
          )
    );

  if (
    filtered.length === 0
  ) {
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
          No Risks Found
        </h2>

        <p
          className="
          text-muted-foreground
          "
        >
          No matching risks.
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
        Risk Center
      </h1>

      <RiskFilters
        search={search}
        setSearch={setSearch}
      />

      <RiskStats
        risks={filtered}
      />

      <RiskCards
        risks={filtered}
        onSelect={
          setSelected
        }
      />

      <RiskTable
        risks={filtered}
        onSelect={
          setSelected
        }
      />

      <RiskDrawer
        risk={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}