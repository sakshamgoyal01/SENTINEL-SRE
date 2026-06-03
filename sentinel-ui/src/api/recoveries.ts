import { api } from "./axios";

export async function getRecoveries() {
  const response =
    await api.get(
      "/recoveries/"
    );

  return response.data;
}