import { api } from "./axios";

export async function getIncidents() {
  const response =
    await api.get(
      "/incidents/"
    );

  return response.data;
}