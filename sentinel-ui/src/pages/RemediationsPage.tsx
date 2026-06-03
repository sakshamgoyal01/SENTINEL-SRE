import { useState } from "react";

import {
  useRemediations,
} from "@/features/remediations/hooks/useRemediations";

import {
  RemediationFilters,
} from "@/features/remediations/components/RemediationFilters";

import {
  RemediationStats,
} from "@/features/remediations/components/RemediationStats";

import {
  RemediationCards,
} from "@/features/remediations/components/RemediationCards";

import {
  RemediationTable,
} from "@/features/remediations/components/RemediationTable";

import {
  RemediationDrawer,
} from "@/features/remediations/components/RemediationDrawer";

export default function RemediationsPage() {
  const {
    data,
    isLoading,
  } = useRemediations();

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

  const remediations =
    data ?? [];

  const filtered =
    remediations.filter(
      (remediation: any) =>
        remediation.service
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
          No Remediations Found
        </h2>

        <p
          className="
          text-muted-foreground
          "
        >
          No matching remediation plans.
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
        Remediation Center
      </h1>

      <RemediationFilters
        search={search}
        setSearch={setSearch}
      />

      <RemediationStats
        remediations={
          filtered
        }
      />

      <RemediationCards
        remediations={
          filtered
        }
        onSelect={
          setSelected
        }
      />

      <RemediationTable
        remediations={
          filtered
        }
        onSelect={
          setSelected
        }
      />

      <RemediationDrawer
        remediation={
          selected
        }
        open={
          !!selected
        }
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}