import { useState } from "react";

import {
  useReports,
} from "@/features/reports/hooks/useReports";

import {
  ReportFilters,
} from "@/features/reports/components/ReportFilters";

import {
  ReportStats,
} from "@/features/reports/components/ReportStats";

import {
  ReportCards,
} from "@/features/reports/components/ReportCards";

import {
  ReportTable,
} from "@/features/reports/components/ReportTable";

import {
  ReportDrawer,
} from "@/features/reports/components/ReportDrawer";

export default function ReportsPage() {

  const {
    data,
    isLoading,
  } =
    useReports();

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

  const reports =
    data ?? [];

  const filtered =
    reports.filter(
      (
        report: any
      ) =>
        report.service
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
        Reports Center
      </h1>

      <ReportFilters
        search={search}
        setSearch={setSearch}
      />

      <ReportStats
        reports={filtered}
      />

      <ReportCards
        reports={filtered}
        onSelect={
          setSelected
        }
      />

      <ReportTable
        reports={filtered}
        onSelect={
          setSelected
        }
      />

      <ReportDrawer
        report={selected}
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
