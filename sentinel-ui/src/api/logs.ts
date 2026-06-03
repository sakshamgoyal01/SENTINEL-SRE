import { api } from "./axios";

export async function getLogs() {
  const response =
    await api.get(
      "/logs/"
    );

  return response.data;
}