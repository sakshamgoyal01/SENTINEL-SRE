import {
  useDashboard,
} from "@/features/dashboard/hooks/useDashboard";

import {
  KPICards,
} from "@/features/dashboard/components/KPICards";

import {
  IncidentTrendChart,
} from "@/features/dashboard/components/IncidentTrendChart";

import {
  RiskDistributionChart,
} from "@/features/dashboard/components/RiskDistributionChart";

import {
  RecentIncidentsTable,
} from "@/features/dashboard/components/RecentIncidentsTable";

import {
  RecentAlertsTable,
} from "@/features/dashboard/components/RecentAlertsTable";

import {
  TopRiskServices,
} from "@/features/dashboard/components/TopRiskServices";

import {
  ExecutionOverview,
} from "@/features/dashboard/components/ExecutionOverview";

import {
  SystemHealth,
} from "@/features/dashboard/components/SystemHealth";

export default function DashboardPage() {
  const {
    alerts,
    incidents,
    risks,
    investigations,
    executions,
    recoveries,
  } = useDashboard();

  const loading =
    alerts.isLoading ||
    incidents.isLoading ||
    risks.isLoading ||
    investigations.isLoading ||
    executions.isLoading ||
    recoveries.isLoading;

  if (loading) {
    return (
      <div
        className="
        flex
        items-center
        justify-center
        h-[70vh]
        "
      >
        Loading Dashboard...
      </div>
    );
  }

  return (
    <div
      className="
      space-y-8
      "
    >
      {/* Header */}

      <div>
        <h1
          className="
          text-4xl
          font-bold
          "
        >
          SENTINEL Command Center
        </h1>

        <p
          className="
          mt-2
          text-muted-foreground
          "
        >
          AI-Powered Autonomous SRE Platform
        </p>
      </div>

      {/* KPI Cards */}

      <KPICards
        alerts={
          alerts.data?.length || 0
        }
        incidents={
          incidents.data?.length || 0
        }
        risks={
          risks.data?.length || 0
        }
        investigations={
          investigations.data?.length || 0
        }
        executions={
          executions.data?.length || 0
        }
        recoveries={
          recoveries.data?.length || 0
        }
      />

      {/* Charts */}

      <div
        className="
        grid
        gap-6
        lg:grid-cols-2
        "
      >
        <IncidentTrendChart
          incidents={
            incidents.data ?? []
          }
        />

        <RiskDistributionChart
          risks={
            risks.data ?? []
          }
        />
      </div>

      {/* Operations Widgets */}

      <div
        className="
        grid
        gap-6
        lg:grid-cols-2
        "
      >
        <RecentIncidentsTable
          incidents={
            incidents.data ?? []
          }
        />

        <RecentAlertsTable
          alerts={
            alerts.data ?? []
          }
        />
      </div>

      {/* Risk Analytics */}

      <TopRiskServices
        risks={
          risks.data ?? []
        }
      />

      {/* Platform Health */}

      <div
        className="
        grid
        gap-6
        lg:grid-cols-2
        "
      >
        <ExecutionOverview
          executions={
            executions.data ?? []
          }
        />

        <SystemHealth
          alerts={
            alerts.data ?? []
          }
          incidents={
            incidents.data ?? []
          }
          risks={
            risks.data ?? []
          }
        />
      </div>
    </div>
  );
}