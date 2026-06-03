import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function MetricDrawer({
  metric,
  open,
  onOpenChange,
}: {
  metric: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {
  if (!metric) {
    return null;
  }

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
            Metric Details
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
              Metric:
            </strong>
            {" "}
            {
              metric.metric_name
            }
          </div>

          <div>
            <strong>
              Value:
            </strong>
            {" "}
            {metric.value}
            {" "}
            {
              metric.unit
            }
          </div>

          <div>
            <strong>
              Service:
            </strong>
            {" "}
            {
              metric.service
            }
          </div>

          <div>
            <strong>
              Cluster:
            </strong>
            {" "}
            {
              metric.cluster
            }
          </div>

          <div>
            <strong>
              Namespace:
            </strong>
            {" "}
            {
              metric.namespace
            }
          </div>

          <div>
            <strong>
              Pod:
            </strong>
            {" "}
            {
              metric.labels
                ?.pod
            }
          </div>

          <div>
            <strong>
              Source:
            </strong>
            {" "}
            {
              metric.source
            }
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}