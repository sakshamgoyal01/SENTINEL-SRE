import { api } from "@/lib/api";

export interface CreateUserPayload {
  email: string;
  username: string;
  password: string;
}

export async function createUser(
  payload: CreateUserPayload
) {
  const response =
    await api.post(
      "/auth/users/",
      payload
    );

  return response.data;
}