import { useState } from "react";

import {
  useKnowledge,
} from "@/features/knowledge/hooks/useKnowledge";

import {
  KnowledgeFilters,
} from "@/features/knowledge/components/KnowledgeFilters";

import {
  KnowledgeStats,
} from "@/features/knowledge/components/KnowledgeStats";

import {
  KnowledgeCards,
} from "@/features/knowledge/components/KnowledgeCards";

import {
  KnowledgeTable,
} from "@/features/knowledge/components/KnowledgeTable";

import {
  KnowledgeDrawer,
} from "@/features/knowledge/components/KnowledgeDrawer";

export default function KnowledgePage() {

  const {
    data,
    isLoading,
  } =
    useKnowledge();

  const [
    search,
    setSearch,
  ] =
    useState("");

  const [
    selected,
    setSelected,
  ] =
    useState<any>(
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

  const entries =
    data ?? [];

  const filtered =
    entries.filter(
      (
        entry: any
      ) =>
        entry.pattern
          ?.incident_type
          ?.toLowerCase()
          .includes(
            search.toLowerCase()
          )
    );

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">
        Knowledge Base
      </h1>

      <KnowledgeFilters
        search={search}
        setSearch={setSearch}
      />

      <KnowledgeStats
        entries={filtered}
      />

      <KnowledgeCards
        entries={filtered}
        onSelect={setSelected}
      />

      <KnowledgeTable
        entries={filtered}
        onSelect={setSelected}
      />

      <KnowledgeDrawer
        entry={selected}
        open={!!selected}
        onOpenChange={() =>
          setSelected(null)
        }
      />
    </div>
  );
}
