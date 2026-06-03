import { Input } from "@/components/ui/input";

export function AlertFilters({
  search,
  setSearch,
}: {
  search: string;
  setSearch: (value: string) => void;
}) {
  return (
    <Input
      placeholder="Search alerts..."
      value={search}
      onChange={(e) =>
        setSearch(e.target.value)
      }
    />
  );
}
