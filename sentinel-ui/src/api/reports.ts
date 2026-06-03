import { api } from "./axios";

export async function getReports() {
  const response =
    await api.get(
      "/reports/"
    );

  return response.data;
}
