import { useState } from "react";

import { useAlerts } from "@/features/alerts/hooks/useAlerts";

import { AlertFilters } from "@/features/alerts/components/AlertFilters";
import { AlertStats } from "@/features/alerts/components/AlertStats";
import { AlertCards } from "@/features/alerts/components/AlertCards";
import { AlertTable } from "@/features/alerts/components/AlertTable";
import { AlertDrawer } from "@/features/alerts/components/AlertDrawer";

export default function AlertsPage() {
  const {
    data,
    isLoading,
  } = useAlerts();

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
    return <div>Loading...</div>;
  }

  const alerts =
    data ?? [];

  const filtered =
    alerts.filter(
      (alert: any) =>
        alert.title
          .toLowerCase()
          .includes(
            search.toLowerCase()
          )
    );

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">
        Alert Center
      </h1>

      <AlertFilters
        search={search}
        setSearch={setSearch}
      />

      <AlertStats
        alerts={filtered}
      />

      <AlertCards
        alerts={filtered}
        onSelect={setSelected}
      />

      <AlertTable
        alerts={filtered}
        onSelect={setSelected}
      />

      <AlertDrawer
        alert={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}
