import { api } from "@/api/axios";

import type {
  LoginRequest,
  TokenResponse,
} from "../types";

export async function login(
  payload: LoginRequest
): Promise<TokenResponse> {

  const response =
    await api.post(
      "/auth/login",
      payload
    );

  return response.data;
}