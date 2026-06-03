import { api } from "./axios";

export async function getKubernetesEvents() {
  const response =
    await api.get(
      "/kubernetes/"
    );

  return response.data;
}