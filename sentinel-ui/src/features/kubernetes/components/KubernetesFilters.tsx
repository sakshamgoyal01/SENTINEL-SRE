import { Input } from "@/components/ui/input";

export function KubernetesFilters({
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
      Search pod...
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