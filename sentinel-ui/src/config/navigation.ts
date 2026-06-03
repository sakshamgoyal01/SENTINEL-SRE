import {
  LayoutDashboard,
  ShieldAlert,
  Search,
  GitBranch,
  AlertTriangle,
  Wrench,
  CheckCircle2,
  PlayCircle,
  RotateCcw,
  Activity,
  FileText,
  Database,
  Boxes,
  Rocket,
  Brain,
  Bell,
  Layers,
  BookOpen,
  Workflow,
  ServerCrash,
} from "lucide-react";

export const navigation = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
    href: "/",
  },

  {
    section: "Detection",

    items: [
      {
        title: "Alerts",
        icon: Bell,
        href: "/alerts",
      },

      {
        title: "Aggregated Events",
        icon: Layers,
        href: "/aggregated-events",
      },
    ],
  },

  {
    section: "Operations",

    items: [
      {
        title: "Incidents",
        icon: ShieldAlert,
        href: "/incidents",
      },

      {
        title: "Investigations",
        icon: Search,
        href: "/investigations",
      },

      {
        title: "Root Causes",
        icon: GitBranch,
        href: "/rootcauses",
      },

      {
        title: "Risks",
        icon: AlertTriangle,
        href: "/risks",
      },

      {
        title: "Knowledge",
        icon: BookOpen,
        href: "/knowledge",
      },

      {
        title: "Remediations",
        icon: Wrench,
        href: "/remediations",
      },

      {
        title: "Approvals",
        icon: CheckCircle2,
        href: "/approvals",
      },

      {
        title: "Executions",
        icon: PlayCircle,
        href: "/executions",
      },

      {
        title: "Verifications",
        icon: CheckCircle2,
        href: "/verifications",
      },

      {
        title: "Recoveries",
        icon: RotateCcw,
        href: "/recoveries",
      },

      {
        title: "Escalations",
        icon: AlertTriangle,
        href: "/escalations",
      },
  {
  title: "States",
  icon: Workflow,
  href: "/states",
},

      {
        title: "Audits",
        icon: FileText,
        href: "/audits",
      },

      {
        title: "Reports",
        icon: Brain,
        href: "/reports",
      },
    ],
  },

  {
    section: "Observability",

    items: [
      {
        title: "Metrics",
        icon: Activity,
        href: "/metrics",
      },

      {
        title: "Logs",
        icon: FileText,
        href: "/logs",
      },

      {
        title: "Traces",
        icon: Database,
        href: "/traces",
      },

      {
        title: "Kubernetes",
        icon: Boxes,
        href: "/kubernetes",
      },

      {
        title: "Deployments",
        icon: Rocket,
        href: "/deployments",
      },
  {
  title: "Processed Telemetry",
  icon: Activity,
  href: "/processed-telemetry",
},
{
  title: "DLQ",
  icon: ServerCrash,
  href: "/dlq",
},
    ],
  },
];