import {
  useForm,
} from "react-hook-form";

import {
  zodResolver,
} from "@hookform/resolvers/zod";

import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import {
  Input,
} from "@/components/ui/input";

import {
  Button,
} from "@/components/ui/button";

import {
  loginSchema,
  type LoginFormValues,
} from "@/features/auth/schemas/loginSchema";

import {
  useLogin,
} from "@/features/auth/hooks/useLogin";

export default function LoginPage() {
  const login =
    useLogin();

  const form =
    useForm<LoginFormValues>({
      resolver:
        zodResolver(
          loginSchema
        ),
    });

  const onSubmit = (
    values: LoginFormValues
  ) => {
    login.mutate(
      values
    );
  };

  return (
    <div
      className="
      flex
      min-h-screen
      items-center
      justify-center
      "
    >
      <Card className="w-96">
        <CardHeader>
          <CardTitle>
            SENTINEL Login
          </CardTitle>
        </CardHeader>

        <CardContent>
          <form
            onSubmit={form.handleSubmit(
              onSubmit
            )}
            className="
            space-y-4
            "
          >
            <Input
              placeholder="Email"
              {...form.register(
                "email"
              )}
            />

            <Input
              type="password"
              placeholder="Password"
              {...form.register(
                "password"
              )}
            />

            <Button
              type="submit"
              className="w-full"
            >
              Login
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}