import { api } from "./axios";

export async function getAggregatedEvents() {
  const response =
    await api.get(
      "/aggregated-events/"
    );

  return response.data;
}
