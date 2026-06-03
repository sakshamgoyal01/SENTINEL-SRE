import {
  createBrowserRouter,
} from "react-router-dom";

import LoginPage from "@/pages/LoginPage";
import DashboardPage from "@/pages/DashboardPage";
import StatesPage from "@/pages/StatesPage";
import ProcessedTelemetryPage from "@/pages/ProcessedTelemetryPage";
import DLQPage from "@/pages/DLQPage";

import IncidentsPage from "@/pages/IncidentsPage";
import InvestigationsPage from "@/pages/InvestigationsPage";
import RootCausesPage from "@/pages/RootCausesPage";
import RisksPage from "@/pages/RisksPage";
import RemediationsPage from "@/pages/RemediationsPage";
import ApprovalsPage from "@/pages/ApprovalsPage";
import ExecutionsPage from "@/pages/ExecutionsPage";
import VerificationsPage from "@/pages/VerificationsPage";
import RecoveriesPage from "@/pages/RecoveriesPage";
import EscalationsPage from "@/pages/EscalationsPage";
import AuditsPage from "@/pages/AuditsPage";
import ReportsPage from "@/pages/ReportsPage";
import KnowledgePage from "@/pages/KnowledgePage";

import AlertsPage from "@/pages/AlertsPage";
import AggregatedEventsPage from "@/pages/AggregatedEventsPage";

import MetricsPage from "@/pages/MetricsPage";
import LogsPage from "@/pages/LogsPage";
import TracesPage from "@/pages/TracesPage";
import KubernetesPage from "@/pages/KubernetesPage";
import DeploymentsPage from "@/pages/DeploymentsPage";

import { AppLayout } from "@/layouts/AppLayout";
import { ProtectedRoute } from "./ProtectedRoute";

export const router =
  createBrowserRouter([
    {
      path: "/login",
      element: <LoginPage />,
    },

    {
      path: "/",

      element: (
        <ProtectedRoute>
          <AppLayout />
        </ProtectedRoute>
      ),

      children: [
        {
          index: true,
          element: <DashboardPage />,
        },

        {
          path: "alerts",
          element: <AlertsPage />,
        },

        {
          path: "aggregated-events",
          element: <AggregatedEventsPage />,
        },

        {
          path: "incidents",
          element: <IncidentsPage />,
        },

        {
          path: "investigations",
          element: <InvestigationsPage />,
        },

        {
          path: "rootcauses",
          element: <RootCausesPage />,
        },

        {
          path: "risks",
          element: <RisksPage />,
        },

        {
          path: "knowledge",
          element: <KnowledgePage />,
        },

        {
          path: "remediations",
          element: <RemediationsPage />,
        },

        {
          path: "approvals",
          element: <ApprovalsPage />,
        },

        {
          path: "executions",
          element: <ExecutionsPage />,
        },

        {
          path: "verifications",
          element: <VerificationsPage />,
        },

        {
          path: "recoveries",
          element: <RecoveriesPage />,
        },

        {
          path: "escalations",
          element: <EscalationsPage />,
        },

        {
          path: "audits",
          element: <AuditsPage />,
        },

        {
          path: "reports",
          element: <ReportsPage />,
        },

        {
          path: "metrics",
          element: <MetricsPage />,
        },

        {
          path: "logs",
          element: <LogsPage />,
        },

        {
          path: "traces",
          element: <TracesPage />,
        },

        {
          path: "kubernetes",
          element: <KubernetesPage />,
        },

        {
          path: "deployments",
          element: <DeploymentsPage />,
        },
    {
  path: "states",
  element: <StatesPage />,
},

{
  path: "processed-telemetry",
  element: <ProcessedTelemetryPage />,
},

{
  path: "dlq",
  element: <DLQPage />,
},
      ],
    },
  ]);