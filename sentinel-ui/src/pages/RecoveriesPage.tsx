import { useState } from "react";

import {
  useRecoveries,
} from "@/features/recoveries/hooks/useRecoveries";

import {
  RecoveryFilters,
} from "@/features/recoveries/components/RecoveryFilters";

import {
  RecoveryStats,
} from "@/features/recoveries/components/RecoveryStats";

import {
  RecoveryCards,
} from "@/features/recoveries/components/RecoveryCards";

import {
  RecoveryTable,
} from "@/features/recoveries/components/RecoveryTable";

import {
  RecoveryDrawer,
} from "@/features/recoveries/components/RecoveryDrawer";

export default function RecoveriesPage() {

  const {
    data,
    isLoading,
  } = useRecoveries();

  const [
    search,
    setSearch,
  ] = useState("");

  const [
    selected,
    setSelected,
  ] = useState<any>(null);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  const recoveries =
    data ?? [];

  const filtered =
    recoveries.filter(
      (recovery: any) =>
        recovery.service
          .toLowerCase()
          .includes(
            search.toLowerCase()
          )
    );

  return (
    <div className="space-y-6">
      <h1
        className="
        text-3xl
        font-bold
        "
      >
        Recovery Center
      </h1>

      <RecoveryFilters
        search={search}
        setSearch={setSearch}
      />

      <RecoveryStats
        recoveries={filtered}
      />

      <RecoveryCards
        recoveries={filtered}
        onSelect={setSelected}
      />

      <RecoveryTable
        recoveries={filtered}
        onSelect={setSelected}
      />

      <RecoveryDrawer
        recovery={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}