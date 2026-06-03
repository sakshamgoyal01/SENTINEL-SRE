import { api } from "./axios";

export async function getKnowledge() {
  const response =
    await api.get(
      "/knowledge/"
    );

  return response.data;
}
