import { api } from "./axios";

export async function getRemediations() {
  const response =
    await api.get(
      "/remediations/"
    );

  return response.data;
}