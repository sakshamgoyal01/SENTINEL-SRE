import { api } from "./axios";

export async function getDLQ() {
  const response =
    await api.get(
      "/dlq/"
    );

  return response.data;
}
