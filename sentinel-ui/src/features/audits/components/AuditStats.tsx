import { Card } from "@/components/ui/card";

export function AuditStats({
  audits,
}: {
  audits: any[];
}) {

  const success =
    audits.filter(
      (audit) =>
        audit.status ===
        "SUCCESS"
    ).length;

  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-4
      "
    >
      <Card className="p-4">
        Audits

        <div className="text-3xl font-bold">
          {audits.length}
        </div>
      </Card>

      <Card className="p-4">
        Success

        <div className="text-3xl font-bold">
          {success}
        </div>
      </Card>

      <Card className="p-4">
        Services

        <div className="text-3xl font-bold">
          {
            new Set(
              audits.map(
                (a) =>
                  a.service
              )
            ).size
          }
        </div>
      </Card>

      <Card className="p-4">
        Success Rate

        <div className="text-3xl font-bold">
          {audits.length
            ? Math.round(
                (success /
                  audits.length) *
                  100
              )
            : 0}
          %
        </div>
      </Card>
    </div>
  );
}