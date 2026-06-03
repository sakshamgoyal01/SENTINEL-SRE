import { Badge } from "@/components/ui/badge";
import { Card } from "@/components/ui/card";

import { SeverityBadge } from "./SeverityBadge";

export function IncidentCards({
  incidents,
  onSelect,
}: {
  incidents: any[];
  onSelect: (incident: any) => void;
}) {
  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-2
      xl:grid-cols-3
      "
    >
      {incidents.map((incident) => (
        <Card
          key={incident.id}
          onClick={() =>
            onSelect(incident)
          }
          className="
          p-4
          cursor-pointer
          hover:border-primary
          transition
          "
        >
          <div
            className="
            flex
            justify-between
            "
          >
            <Badge>
              {
                incident
                  .incident_priority
              }
            </Badge>

            <SeverityBadge
              severity={
                incident
                  .aggregated_event
                  ?.severity
              }
            />
          </div>

          <h3
            className="
            mt-3
            font-semibold
            "
          >
            {incident.service}
          </h3>

          <p
            className="
            text-sm
            text-muted-foreground
            "
          >
            {
              incident
                .aggregated_event
                ?.summary
            }
          </p>

          <div
            className="
            mt-4
            space-y-2
            text-sm
            "
          >
            <div>
              Risk:
              {" "}
              {
                incident
                  .final_risk_score
              }
            </div>

            <div>
              Impact:
              {" "}
              {
                incident
                  .impact_score
              }
            </div>

            <div>
              Escalation:
              {" "}
              {incident.escalation_required
                ? "Yes"
                : "No"}
            </div>

            <div>
              Human Review:
              {" "}
              {incident.requires_human_review
                ? "Yes"
                : "No"}
            </div>
          </div>
        </Card>
      ))}
    </div>
  );
}