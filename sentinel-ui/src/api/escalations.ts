import { api } from "./axios";

export async function getEscalations() {
  const response =
    await api.get(
      "/escalations/"
    );

  return response.data;
}