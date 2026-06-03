import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";

export function DeploymentDrawer({
  deployment,
  open,
  onOpenChange,
}: {
  deployment: any;

  open: boolean;

  onOpenChange: (
    value: boolean
  ) => void;
}) {
  if (!deployment) {
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
            Deployment Details
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
              Deployment:
            </strong>
            {" "}
            {
              deployment
                .deployment_name
            }
          </div>

          <div>
            <strong>
              Image:
            </strong>
            {" "}
            {
              deployment.image
            }
          </div>

          <div>
            <strong>
              Namespace:
            </strong>
            {" "}
            {
              deployment.namespace
            }
          </div>

          <div>
            <strong>
              Replicas:
            </strong>
            {" "}
            {
              deployment.replicas
            }
          </div>

          <div>
            <strong>
              Available:
            </strong>
            {" "}
            {
              deployment
                .available_replicas
            }
          </div>

          <div>
            <strong>
              Updated:
            </strong>
            {" "}
            {
              deployment
                .updated_replicas
            }
          </div>

          <div>
            <strong>
              Strategy:
            </strong>
            {" "}
            {
              deployment.strategy
            }
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}