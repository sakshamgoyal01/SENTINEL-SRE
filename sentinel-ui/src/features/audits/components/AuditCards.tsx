import { Card } from "@/components/ui/card";

export function AuditCards({
  audits,
  onSelect,
}: {
  audits: any[];

  onSelect: (
    audit: any
  ) => void;
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
      {audits.map(
        (audit) => (
          <Card
            key={audit.id}
            className="
            p-4
            cursor-pointer
            "
            onClick={() =>
              onSelect(
                audit
              )
            }
          >
            <div
              className="
              flex
              justify-between
              "
            >
              <div
                className="
                font-bold
                "
              >
                {
                  audit.status
                }
              </div>
            </div>

            <div
              className="
              mt-3
              text-lg
              font-semibold
              "
            >
              {
                audit.service
              }
            </div>

            <div
              className="
              mt-2
              text-sm
              "
            >
              {
                audit.details
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}