import { useState } from "react";

import {
  useStates,
} from "@/features/states/hooks/useStates";

import {
  StateFilters,
} from "@/features/states/components/StateFilters";

import {
  StateStats,
} from "@/features/states/components/StateStats";

import {
  StateCards,
} from "@/features/states/components/StateCards";

import {
  StateTable,
} from "@/features/states/components/StateTable";

import {
  StateDrawer,
} from "@/features/states/components/StateDrawer";

export default function StatesPage() {

  const {
    data,
    isLoading,
  } = useStates();

  const [
    search,
    setSearch,
  ] = useState("");

  const [
    selected,
    setSelected,
  ] = useState<any>(
    null
  );

  if (
    isLoading
  ) {
    return (
      <div>
        Loading...
      </div>
    );
  }

  const states =
    data ?? [];

  const filtered =
    states.filter(
      (state: any) =>
        state.service
          .toLowerCase()
          .includes(
            search.toLowerCase()
          )
    );

  return (
    <div
      className="
      space-y-6
      "
    >
      <h1
        className="
        text-3xl
        font-bold
        "
      >
        Incident States
      </h1>

      <StateFilters
        search={search}
        setSearch={setSearch}
      />

      <StateStats
        states={filtered}
      />

      <StateCards
        states={filtered}
        onSelect={
          setSelected
        }
      />

      <StateTable
        states={filtered}
        onSelect={
          setSelected
        }
      />

      <StateDrawer
        state={selected}
        open={
          !!selected
        }
        onOpenChange={() =>
          setSelected(
            null
          )
        }
      />
    </div>
  );
}
