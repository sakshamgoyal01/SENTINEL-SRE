import { api } from "./axios";

export async function getDeployments() {
  const response =
    await api.get(
      "/deployments/"
    );

  return response.data;
}