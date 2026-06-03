import { ThemeToggle } from "./ThemeToggle";
import { Button } from "@/components/ui/button";
import { useAuthStore } from "@/store/authStore";

export function Navbar() {
  const logout = useAuthStore(
    (s) => s.logout
  );

  return (
    <header
      className="
      h-16
      border-b
      flex
      items-center
      justify-between
      px-6
      "
    >
      <div>
        AI-Powered SRE Platform
      </div>

      <div className="flex items-center gap-2">
        <ThemeToggle />

        <Button
          variant="outline"
          onClick={logout}
        >
          Logout
        </Button>
      </div>
    </header>
  );
}