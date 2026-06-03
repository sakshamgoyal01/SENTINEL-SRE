from pydantic import BaseModel


class AssignRoleRequest(
    BaseModel
):

    user_id: str

    role_id: str