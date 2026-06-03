import { useState } from "react";

import {
  useDeployments,
} from "@/features/deployments/hooks/useDeployments";

import {
  DeploymentFilters,
} from "@/features/deployments/components/DeploymentFilters";

import {
  DeploymentStats,
} from "@/features/deployments/components/DeploymentStats";

import {
  DeploymentCards,
} from "@/features/deployments/components/DeploymentCards";

import {
  DeploymentTable,
} from "@/features/deployments/components/DeploymentTable";

import {
  DeploymentDrawer,
} from "@/features/deployments/components/DeploymentDrawer";

export default function DeploymentsPage() {

  const {
    data,
    isLoading,
  } = useDeployments();

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

  const deployments =
    data ?? [];

  const filtered =
    deployments.filter(
      (deployment: any) =>
        deployment
          .deployment_name
          .toLowerCase()
          .includes(
            search.toLowerCase()
          )
    );

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">
        Deployment Center
      </h1>

      <DeploymentFilters
        search={search}
        setSearch={setSearch}
      />

      <DeploymentStats
        deployments={filtered}
      />

      <DeploymentCards
        deployments={filtered}
        onSelect={setSelected}
      />

      <DeploymentTable
        deployments={filtered}
        onSelect={setSelected}
      />

      <DeploymentDrawer
        deployment={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}