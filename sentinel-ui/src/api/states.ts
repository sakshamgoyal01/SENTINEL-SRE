import { api } from "./axios";

export async function getStates() {
  const response =
    await api.get(
      "/states/"
    );

  return response.data;
}
