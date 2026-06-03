import { useState } from "react";

import {
  useKubernetes,
} from "@/features/kubernetes/hooks/useKubernetes";

import {
  KubernetesFilters,
} from "@/features/kubernetes/components/KubernetesFilters";

import {
  KubernetesStats,
} from "@/features/kubernetes/components/KubernetesStats";

import {
  KubernetesCards,
} from "@/features/kubernetes/components/KubernetesCards";

import {
  KubernetesTable,
} from "@/features/kubernetes/components/KubernetesTable";

import {
  KubernetesDrawer,
} from "@/features/kubernetes/components/KubernetesDrawer";

export default function KubernetesPage() {

  const {
    data,
    isLoading,
  } = useKubernetes();

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

  const events =
    data ?? [];

  const filtered =
    events.filter(
      (event: any) =>
        event
          .involved_object
          ?.name
          ?.toLowerCase()
          .includes(
            search.toLowerCase()
          )
    );

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">
        Kubernetes Event Center
      </h1>

      <KubernetesFilters
        search={search}
        setSearch={setSearch}
      />

      <KubernetesStats
        events={filtered}
      />

      <KubernetesCards
        events={filtered}
        onSelect={setSelected}
      />

      <KubernetesTable
        events={filtered}
        onSelect={setSelected}
      />

      <KubernetesDrawer
        event={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}