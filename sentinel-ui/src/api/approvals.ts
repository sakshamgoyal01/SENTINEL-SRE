import { api } from "./axios";

export async function getApprovals() {
  const response =
    await api.get(
      "/approvals/"
    );

  return response.data;
}