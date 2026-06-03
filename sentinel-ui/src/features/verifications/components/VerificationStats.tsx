import { Card } from "@/components/ui/card";

export function VerificationStats({
  verifications,
}: {
  verifications: any[];
}) {

  const successful =
    verifications.filter(
      (v) =>
        v.verification_result ===
        "SUCCESS"
    ).length;

  const healthy =
    verifications.filter(
      (v) =>
        v.health_status ===
        "HEALTHY"
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
        Total

        <div className="text-3xl font-bold">
          {verifications.length}
        </div>
      </Card>

      <Card className="p-4">
        Success

        <div className="text-3xl font-bold">
          {successful}
        </div>
      </Card>

      <Card className="p-4">
        Healthy

        <div className="text-3xl font-bold">
          {healthy}
        </div>
      </Card>

      <Card className="p-4">
        Success Rate

        <div className="text-3xl font-bold">
          {verifications.length
            ? Math.round(
                (successful /
                  verifications.length) *
                  100
              )
            : 0}
          %
        </div>
      </Card>
    </div>
  );
}