from backend.auth.permissions import (
    RequireRole
)

from backend.auth.roles import (
    RoleName
)

RequireAdmin = (
    RequireRole(
        RoleName.ADMIN
    )
)

RequireSRE = (
    RequireRole(
        RoleName.SRE
    )
)

RequireEngineer = (
    RequireRole(
        RoleName.ENGINEER
    )
)

RequireViewer = (
    RequireRole(
        RoleName.VIEWER
    )
)