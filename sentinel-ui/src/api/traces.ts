import { api } from "./axios";

export async function getTraces() {
  const response =
    await api.get(
      "/traces/"
    );

  return response.data;
}