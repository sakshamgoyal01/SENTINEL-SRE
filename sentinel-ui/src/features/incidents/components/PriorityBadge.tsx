import { Badge } from "@/components/ui/badge";

export function PriorityBadge({
  priority,
}: {
  priority: string;
}) {
  switch (priority) {
    case "P1":
      return (
        <Badge variant="destructive">
          P1
        </Badge>
      );

    case "P2":
      return (
        <Badge
          className="
          bg-orange-500
          text-white
          "
        >
          P2
        </Badge>
      );

    case "P3":
      return (
        <Badge
          className="
          bg-yellow-500
          text-black
          "
        >
          P3
        </Badge>
      );

    default:
      return (
        <Badge variant="secondary">
          {priority}
        </Badge>
      );
  }
}