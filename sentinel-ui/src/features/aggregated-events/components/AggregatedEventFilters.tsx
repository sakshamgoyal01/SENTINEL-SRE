import { Input } from "@/components/ui/input";

export function AggregatedEventFilters({
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
      placeholder="Search events..."
      value={search}
      onChange={(e) =>
        setSearch(
          e.target.value
        )
      }
    />
  );
}
