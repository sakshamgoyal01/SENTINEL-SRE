import { api } from "@/lib/api";
import { User } from "../types";

export async function getUsers() {
  const response =
    await api.get<User[]>(
      "/auth/users/"
    );

  return response.data;
}