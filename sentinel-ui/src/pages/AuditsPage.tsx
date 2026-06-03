import { useState } from "react";

import {
  useAudits,
} from "@/features/audits/hooks/useAudits";

import {
  AuditFilters,
} from "@/features/audits/components/AuditFilters";

import {
  AuditStats,
} from "@/features/audits/components/AuditStats";

import {
  AuditCards,
} from "@/features/audits/components/AuditCards";

import {
  AuditTable,
} from "@/features/audits/components/AuditTable";

import {
  AuditDrawer,
} from "@/features/audits/components/AuditDrawer";

export default function AuditsPage() {

  const {
    data,
    isLoading,
  } = useAudits();

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

  const audits =
    data ?? [];

  const filtered =
    audits.filter(
      (audit: any) =>
        audit.service
          .toLowerCase()
          .includes(
            search.toLowerCase()
          )
    );

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">
        Audit Center
      </h1>

      <AuditFilters
        search={search}
        setSearch={setSearch}
      />

      <AuditStats
        audits={filtered}
      />

      <AuditCards
        audits={filtered}
        onSelect={setSelected}
      />

      <AuditTable
        audits={filtered}
        onSelect={setSelected}
      />

      <AuditDrawer
        audit={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}