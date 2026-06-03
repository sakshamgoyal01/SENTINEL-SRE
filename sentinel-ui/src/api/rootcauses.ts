import { api } from "./axios";

export async function getRootCauses() {
  const response =
    await api.get(
      "/rootcauses/"
    );

  return response.data;
}