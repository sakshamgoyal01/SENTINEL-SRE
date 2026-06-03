import { Input } from "@/components/ui/input";

interface Props {
  search: string;
  setSearch: (
    value: string
  ) => void;
}

export function InvestigationFilters({
  search,
  setSearch,
}: Props) {
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