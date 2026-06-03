import { Card } from "@/components/ui/card";

export function DeploymentStats({
  deployments,
}: {
  deployments: any[];
}) {

  const totalReplicas =
    deployments.reduce(
      (
        total,
        deployment
      ) =>
        total +
        deployment.replicas,
      0
    );

  const available =
    deployments.reduce(
      (
        total,
        deployment
      ) =>
        total +
        deployment.available_replicas,
      0
    );

  return (
    <div
      className="
      grid
      gap-4
      md:grid-cols-4
      "
    >
      <Card className="p-4">
        Deployments

        <div className="text-3xl font-bold">
          {deployments.length}
        </div>
      </Card>

      <Card className="p-4">
        Replicas

        <div className="text-3xl font-bold">
          {totalReplicas}
        </div>
      </Card>

      <Card className="p-4">
        Available

        <div className="text-3xl font-bold">
          {available}
        </div>
      </Card>

      <Card className="p-4">
        Namespaces

        <div className="text-3xl font-bold">
          {
            new Set(
              deployments.map(
                (d) =>
                  d.namespace
              )
            ).size
          }
        </div>
      </Card>
    </div>
  );
}