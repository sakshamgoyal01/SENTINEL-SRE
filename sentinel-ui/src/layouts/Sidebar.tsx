import { Link } from "react-router-dom";
import { navigation } from "@/config/navigation";

export function Sidebar() {
  return (
    <aside
      className="
      w-72
      border-r
      p-4
      overflow-y-auto
      "
    >
      <div
        className="
        text-xl
        font-bold
        mb-8
        "
      >
        SENTINEL
      </div>

      {navigation.map(
        (group, idx) => {

          if ("section" in group) {
            return (
              <div
                key={idx}
                className="mb-6"
              >
                <div
                  className="
                  text-xs
                  uppercase
                  text-muted-foreground
                  mb-2
                  "
                >
                  {group.section}
                </div>

                <div className="space-y-1">
                  {group.items.map(
                    (item) => (
                      <Link
                        key={item.href}
                        to={item.href}
                        className="
                        flex
                        items-center
                        gap-2
                        rounded-md
                        px-3
                        py-2
                        hover:bg-muted
                        "
                      >
                        <item.icon
                          className="
                          h-4
                          w-4
                          "
                        />

                        {item.title}
                      </Link>
                    )
                  )}
                </div>
              </div>
            );
          }

          return (
            <Link
              key={group.href}
              to={group.href}
              className="
              flex
              items-center
              gap-2
              rounded-md
              px-3
              py-2
              mb-4
              hover:bg-muted
              "
            >
              <group.icon
                className="
                h-4
                w-4
                "
              />

              {group.title}
            </Link>
          );
        }
      )}
    </aside>
  );
}