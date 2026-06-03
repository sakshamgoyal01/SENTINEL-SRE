import { Card } from "@/components/ui/card";

export function DeploymentCards({
  deployments,
  onSelect,
}: {
  deployments: any[];

  onSelect: (
    deployment: any
  ) => void;
}) {
  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-2
      "
    >
      {deployments.map(
        (deployment) => (
          <Card
            key={deployment.id}
            className="
            p-4
            cursor-pointer
            "
            onClick={() =>
              onSelect(
                deployment
              )
            }
          >
            <h3 className="font-bold">
              {
                deployment
                  .deployment_name
              }
            </h3>

            <div className="mt-2">
              {
                deployment.image
              }
            </div>

            <div className="mt-2">
              Replicas:
              {" "}
              {
                deployment.replicas
              }
            </div>

            <div className="mt-2">
              Available:
              {" "}
              {
                deployment
                  .available_replicas
              }
            </div>
          </Card>
        )
      )}
    </div>
  );
}