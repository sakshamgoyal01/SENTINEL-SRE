import { useMutation } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";

import { login } from "../api/auth";
import { useAuthStore } from "@/store/authStore";

export function useLogin() {
  const navigate = useNavigate();

  const setToken = useAuthStore(
    (s) => s.setToken
  );

  return useMutation({
    mutationFn: login,

    onSuccess: (response) => {
      console.log(
        "LOGIN SUCCESS",
        response
      );

      setToken(
        response.access_token
      );

      navigate("/");
    },

    onError: (error) => {
      console.error(
        "LOGIN FAILED",
        error
      );
    },
  });
}