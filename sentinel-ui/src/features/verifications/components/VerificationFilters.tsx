import { Input } from "@/components/ui/input";

export function VerificationFilters({
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
      Search service...
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