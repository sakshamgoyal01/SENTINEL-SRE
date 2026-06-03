from fastapi import (
    Depends,
    HTTPException,
    status,
)

from backend.auth.current_user import (
    get_current_user,
)


ROLE_HIERARCHY = {
    "VIEWER": 1,
    "ENGINEER": 2,
    "SRE": 3,
    "ADMIN": 4,
}


class RequireRole:

    def __init__(
        self,
        role: str,
    ):
        self.role = role

    async def __call__(
        self,
        user=Depends(
            get_current_user
        ),
    ):
        user_roles = user.get(
            "roles",
            []
        )

        if not user_roles:

            raise HTTPException(
                status_code=
                status.HTTP_403_FORBIDDEN,
                detail=
                "No roles assigned",
            )

        required_level = (
            ROLE_HIERARCHY.get(
                str(self.role),
                999,
            )
        )

        highest_user_level = max(
            ROLE_HIERARCHY.get(
                str(role),
                0,
            )
            for role in user_roles
        )

        if highest_user_level < required_level:

            raise HTTPException(
                status_code=
                status.HTTP_403_FORBIDDEN,
                detail=
                "Insufficient role",
            )

        return user