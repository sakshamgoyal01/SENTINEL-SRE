import { Card } from "@/components/ui/card";

export function VerificationCards({
  verifications,
  onSelect,
}: {
  verifications: any[];

  onSelect: (
    verification: any
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
      {verifications.map(
        (
          verification
        ) => (
          <Card
            key={
              verification.id
            }
            className="
            p-4
            cursor-pointer
            "
            onClick={() =>
              onSelect(
                verification
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
                  verification
                    .verification_result
                }
              </div>

              <div>
                {
                  verification
                    .health_status
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
                verification.service
              }
            </div>

            <div
              className="
              mt-2
              text-sm
              text-muted-foreground
              "
            >
              Verified:
              {" "}
              {
                verification.verified
                  ? "Yes"
                  : "No"
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}