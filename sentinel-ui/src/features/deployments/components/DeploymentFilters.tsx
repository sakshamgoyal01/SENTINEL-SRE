import { Input } from "@/components/ui/input";

export function DeploymentFilters({
  search,
  setSearch,
}: {
  search: string;

  setSearch: (
    value: string
  ) => void;
}) {
  return (
    <Input
      placeholder="
      Search deployment...
      "
      value={search}
      onChange={(e) =>
        setSearch(
          e.target.value
        )
      }
    />
  );
}