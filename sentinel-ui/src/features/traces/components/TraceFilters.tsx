import { Input } from "@/components/ui/input";

export function TraceFilters({
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
      Search operation...
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