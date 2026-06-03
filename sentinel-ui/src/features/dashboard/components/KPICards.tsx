import {
  ShieldAlert,
  AlertTriangle,
  Search,
  PlayCircle,
  RotateCcw,
  Bell,
} from "lucide-react";

import {
  Card,
} from "@/components/ui/card";

export function KPICards({
  alerts,
  incidents,
  risks,
  investigations,
  executions,
  recoveries,
}: any) {

  const cards = [
    {
      title: "Alerts",
      value: alerts,
      icon: Bell,
    },

    {
      title: "Incidents",
      value: incidents,
      icon:
        ShieldAlert,
    },

    {
      title: "Risks",
      value: risks,
      icon:
        AlertTriangle,
    },

    {
      title:
        "Investigations",
      value:
        investigations,
      icon: Search,
    },

    {
      title:
        "Executions",
      value:
        executions,
      icon:
        PlayCircle,
    },

    {
      title:
        "Recoveries",
      value:
        recoveries,
      icon:
        RotateCcw,
    },
  ];

  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-3
      xl:grid-cols-6
      "
    >
      {cards.map(
        (card) => {

          const Icon =
            card.icon;

          return (
            <Card
              key={
                card.title
              }
              className="
              p-5
              transition-all
              hover:shadow-lg
              "
            >
              <div
                className="
                flex
                items-center
                justify-between
                "
              >
                <div>
                  <p
                    className="
                    text-sm
                    text-muted-foreground
                    "
                  >
                    {
                      card.title
                    }
                  </p>

                  <h2
                    className="
                    mt-2
                    text-4xl
                    font-bold
                    "
                  >
                    {
                      card.value
                    }
                  </h2>
                </div>

                <Icon
                  className="
                  h-8
                  w-8
                  text-muted-foreground
                  "
                />
              </div>
            </Card>
          );
        }
      )}
    </div>
  );
}