import { QueryProvider } from "./QueryProvider";
import { ThemeProvider } from "./ThemeProvider";

import { ReactNode } from "react";

export function AppProviders({
  children,
}: {
  children: ReactNode;
}) {
  return (
    <ThemeProvider>
      <QueryProvider>
        {children}
      </QueryProvider>
    </ThemeProvider>
  );
}