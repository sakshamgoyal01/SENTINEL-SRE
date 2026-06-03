import { Badge } from "@/components/ui/badge";

export function SeverityBadge({
  severity,
}: {
  severity: string;
}) {
  switch (severity) {
    case "CRITICAL":
      return (
        <Badge variant="destructive">
          CRITICAL
        </Badge>
      );

    case "HIGH":
      return (
        <Badge
          className="
          bg-orange-500
          text-white
          "
        >
          HIGH
        </Badge>
      );

    case "MEDIUM":
      return (
        <Badge
          className="
          bg-yellow-500
          text-black
          "
        >
          MEDIUM
        </Badge>
      );

    default:
      return (
        <Badge variant="secondary">
          LOW
        </Badge>
      );
  }
}