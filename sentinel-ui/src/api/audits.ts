import { api } from "./axios";

export async function getAudits() {
  const response =
    await api.get(
      "/audits/"
    );

  return response.data;
}