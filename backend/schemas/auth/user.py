from pydantic import BaseModel
from pydantic import EmailStr
from uuid import UUID

class CreateUserRequest(
    BaseModel
):

    email: EmailStr

    username: str

    password: str


class UserResponse(
    BaseModel
):

    id: UUID

    email: str

    username: str

    is_active: bool

    is_superuser: bool

    model_config = {
        "from_attributes": True
    }