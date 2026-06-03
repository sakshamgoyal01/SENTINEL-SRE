import { api } from "./axios";

export async function getExecutions() {
  const response =
    await api.get(
      "/executions/"
    );

  return response.data;
}