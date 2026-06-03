import { useState } from "react";

import {
  useVerifications,
} from "@/features/verifications/hooks/useVerifications";

import {
  VerificationFilters,
} from "@/features/verifications/components/VerificationFilters";

import {
  VerificationStats,
} from "@/features/verifications/components/VerificationStats";

import {
  VerificationCards,
} from "@/features/verifications/components/VerificationCards";

import {
  VerificationTable,
} from "@/features/verifications/components/VerificationTable";

import {
  VerificationDrawer,
} from "@/features/verifications/components/VerificationDrawer";

export default function VerificationsPage() {

  const {
    data,
    isLoading,
  } =
    useVerifications();

  const [
    search,
    setSearch,
  ] =
    useState("");

  const [
    selected,
    setSelected,
  ] =
    useState<any>(
      null
    );

  if (
    isLoading
  ) {
    return (
      <div>
        Loading...
      </div>
    );
  }

  const verifications =
    data ?? [];

  const filtered =
    verifications.filter(
      (
        verification: any
      ) =>
        verification.service
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
        Verification Center
      </h1>

      <VerificationFilters
        search={search}
        setSearch={
          setSearch
        }
      />

      <VerificationStats
        verifications={
          filtered
        }
      />

      <VerificationCards
        verifications={
          filtered
        }
        onSelect={
          setSelected
        }
      />

      <VerificationTable
        verifications={
          filtered
        }
        onSelect={
          setSelected
        }
      />

      <VerificationDrawer
        verification={
          selected
        }
        open={
          !!selected
        }
        onOpenChange={() =>
          setSelected(
            null
          )
        }
      />
    </div>
  );
}