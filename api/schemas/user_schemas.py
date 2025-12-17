from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    email: EmailStr


class UserResponse(BaseModel):
    id: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def from_entity(cls, user):
        return cls(
            id=user.id,
            email=user.email.value
        )
