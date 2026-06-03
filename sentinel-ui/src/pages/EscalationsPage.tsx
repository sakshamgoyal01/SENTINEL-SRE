import { useState } from "react";

import {
  useEscalations,
} from "@/features/escalations/hooks/useEscalations";

import {
  EscalationFilters,
} from "@/features/escalations/components/EscalationFilters";

import {
  EscalationStats,
} from "@/features/escalations/components/EscalationStats";

import {
  EscalationCards,
} from "@/features/escalations/components/EscalationCards";

import {
  EscalationTable,
} from "@/features/escalations/components/EscalationTable";

import {
  EscalationDrawer,
} from "@/features/escalations/components/EscalationDrawer";

export default function EscalationsPage() {

  const {
    data,
    isLoading,
  } = useEscalations();

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

  const escalations =
    data ?? [];

  const filtered =
    escalations.filter(
      (e: any) =>
        e.service
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
        Escalation Center
      </h1>

      <EscalationFilters
        search={search}
        setSearch={setSearch}
      />

      <EscalationStats
        escalations={filtered}
      />

      <EscalationCards
        escalations={filtered}
        onSelect={setSelected}
      />

      <EscalationTable
        escalations={filtered}
        onSelect={setSelected}
      />

      <EscalationDrawer
        escalation={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(
            null
          )
        }
      />
    </div>
  );
}