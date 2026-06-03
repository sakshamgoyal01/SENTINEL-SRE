import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function DeploymentTable({
  deployments,
  onSelect,
}: {
  deployments: any[];

  onSelect: (
    deployment: any
  ) => void;
}) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>
            Deployment
          </TableHead>

          <TableHead>
            Image
          </TableHead>

          <TableHead>
            Replicas
          </TableHead>

          <TableHead>
            Available
          </TableHead>

          <TableHead>
            Strategy
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {deployments.map(
          (deployment) => (
            <TableRow
              key={
                deployment.id
              }
              onClick={() =>
                onSelect(
                  deployment
                )
              }
              className="
              cursor-pointer
              "
            >
              <TableCell>
                {
                  deployment
                    .deployment_name
                }
              </TableCell>

              <TableCell>
                {
                  deployment.image
                }
              </TableCell>

              <TableCell>
                {
                  deployment.replicas
                }
              </TableCell>

              <TableCell>
                {
                  deployment
                    .available_replicas
                }
              </TableCell>

              <TableCell>
                {
                  deployment.strategy
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}