import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function IncidentDrawer({
  incident,
  open,
  onOpenChange,
}: {
  incident: any;
  open: boolean;
  onOpenChange: (
    value: boolean
  ) => void;
}) {

  if (!incident)
    return null;

  return (
    <Sheet
      open={open}
      onOpenChange={
        onOpenChange
      }
    >
      <SheetContent>
        <SheetHeader>
          <SheetTitle>
            Incident Details
          </SheetTitle>
        </SheetHeader>

        <div
          className="
          mt-6
          space-y-4
          "
        >
          <div>
            <strong>
              Service:
            </strong>
            {" "}
            {
              incident.service
            }
          </div>

          <div>
            <strong>
              Priority:
            </strong>
            {" "}
            {
              incident
                .incident_priority
            }
          </div>

          <div>
            <strong>
              Severity:
            </strong>
            {" "}
            {
              incident
                .aggregated_event
                ?.severity
            }
          </div>

          <div>
            <strong>
              Summary:
            </strong>
            {" "}
            {
              incident
                .aggregated_event
                ?.summary
            }
          </div>

          <div>
            <strong>
              Category:
            </strong>
            {" "}
            {
              incident
                .aggregated_event
                ?.category
            }
          </div>

          <div>
            <strong>
              Risk:
            </strong>
            {" "}
            {
              incident
                .final_risk_score
            }
          </div>

          <div>
            <strong>
              Impact:
            </strong>
            {" "}
            {
              incident
                .impact_score
            }
          </div>

          <div>
            <strong>
              Event Count:
            </strong>
            {" "}
            {
              incident
                .aggregated_event
                ?.count
            }
          </div>

          <div>
            <strong>
              Escalation:
            </strong>
            {" "}
            {
              incident
                .escalation_required
                ? "Yes"
                : "No"
            }
          </div>

          <div>
            <strong>
              Human Review:
            </strong>
            {" "}
            {
              incident
                .requires_human_review
                ? "Yes"
                : "No"
            }
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}