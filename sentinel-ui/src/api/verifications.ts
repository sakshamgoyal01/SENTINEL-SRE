import { api } from "./axios";

export async function getVerifications() {
  const response =
    await api.get(
      "/verifications/"
    );

  return response.data;
}