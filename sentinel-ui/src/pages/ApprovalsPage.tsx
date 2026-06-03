import { useState } from "react";

import {
  useApprovals,
} from "@/features/approvals/hooks/useApprovals";

import {
  ApprovalFilters,
} from "@/features/approvals/components/ApprovalFilters";

import {
  ApprovalStats,
} from "@/features/approvals/components/ApprovalStats";

import {
  ApprovalCards,
} from "@/features/approvals/components/ApprovalCards";

import {
  ApprovalTable,
} from "@/features/approvals/components/ApprovalTable";

import {
  ApprovalDrawer,
} from "@/features/approvals/components/ApprovalDrawer";

export default function ApprovalsPage() {
  const {
    data,
    isLoading,
  } = useApprovals();

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

  const approvals =
    data ?? [];

  const filtered =
    approvals.filter(
      (approval: any) =>
        approval.service
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
          No Approvals Found
        </h2>

        <p
          className="
          text-muted-foreground
          "
        >
          No matching approvals.
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
        Approval Center
      </h1>

      <ApprovalFilters
        search={search}
        setSearch={setSearch}
      />

      <ApprovalStats
        approvals={filtered}
      />

      <ApprovalCards
        approvals={filtered}
        onSelect={
          setSelected
        }
      />

      <ApprovalTable
        approvals={filtered}
        onSelect={
          setSelected
        }
      />

      <ApprovalDrawer
        approval={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}