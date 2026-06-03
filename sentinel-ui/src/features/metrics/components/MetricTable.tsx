import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export function MetricTable({
  metrics,
  onSelect,
}: {
  metrics: any[];

  onSelect: (
    metric: any
  ) => void;
}) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>
            Metric
          </TableHead>

          <TableHead>
            Service
          </TableHead>

          <TableHead>
            Value
          </TableHead>

          <TableHead>
            Source
          </TableHead>

          <TableHead>
            Cluster
          </TableHead>
        </TableRow>
      </TableHeader>

      <TableBody>
        {metrics.map(
          (metric) => (
            <TableRow
              key={metric.id}
              className="
              cursor-pointer
              "
              onClick={() =>
                onSelect(
                  metric
                )
              }
            >
              <TableCell>
                {
                  metric.metric_name
                }
              </TableCell>

              <TableCell>
                {
                  metric.service
                }
              </TableCell>

              <TableCell>
                {metric.value}
                {" "}
                {
                  metric.unit
                }
              </TableCell>

              <TableCell>
                {
                  metric.source
                }
              </TableCell>

              <TableCell>
                {
                  metric.cluster
                }
              </TableCell>
            </TableRow>
          )
        )}
      </TableBody>
    </Table>
  );
}