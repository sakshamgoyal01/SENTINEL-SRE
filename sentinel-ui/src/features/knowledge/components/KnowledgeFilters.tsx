import { Input } from "@/components/ui/input";

export function KnowledgeFilters({
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
      placeholder="Search incident type..."
      value={search}
      onChange={(e) =>
        setSearch(
          e.target.value
        )
      }
    />
  );
}
