import { api } from "./axios";

export async function getRisks() {
  const response =
    await api.get(
      "/risks/"
    );

  return response.data;
}