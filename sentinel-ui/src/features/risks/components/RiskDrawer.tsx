import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function RiskDrawer({
  risk,
  open,
  onOpenChange,
}: {
  risk: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {
  if (!risk) {
    return null;
  }

  const impacted =
    risk.blast_radius
      ?.impacted_services ??
    risk.blast_radius
      ?.services ??
    [];

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
            Risk Details
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
            {risk.service}
          </div>

          <div>
            <strong>
              Priority:
            </strong>
            {" "}
            {risk.priority}
          </div>

          <div>
            <strong>
              Risk Level:
            </strong>
            {" "}
            {
              risk
                .risk_summary
                ?.risk_level
            }
          </div>

          <div>
            <strong>
              Customer Impact:
            </strong>
            {" "}
            {
              risk
                .impact_assessment
                ?.customer_impact
            }
          </div>

          <div>
            <strong>
              Root Cause ID:
            </strong>
            {" "}
            {risk.rootcause_id}
          </div>

          <div>
            <strong>
              Impacted Services:
            </strong>

            <ul
              className="
              mt-2
              list-disc
              pl-5
              "
            >
              {impacted.map(
                (
                  service: string
                ) => (
                  <li
                    key={
                      service
                    }
                  >
                    {service}
                  </li>
                )
              )}
            </ul>
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}