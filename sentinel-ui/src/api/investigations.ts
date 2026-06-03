import { api } from "./axios";

export async function getInvestigations() {
  const response =
    await api.get(
      "/investigations/"
    );

  return response.data;
}