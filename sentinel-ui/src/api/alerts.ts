import { api } from "./axios";

export async function getAlerts() {
  const response =
    await api.get(
      "/alerts/"
    );

  return response.data;
}
