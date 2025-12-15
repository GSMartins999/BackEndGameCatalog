from fastapi import APIRouter, Depends, HTTPException

from api.dependencies import get_current_user, get_use_case_factory
from api.schemas.user_schemas import UserCreate, UserResponse
from core.domain.entities import User
from core.factories.use_case_factory import UseCaseFactory

user_router = APIRouter()


@user_router.post("/users")
async def create_user(
    user: UserCreate, factory: UseCaseFactory = Depends(get_use_case_factory)
):
    try:
        register_user_use_case = factory.create_register_user()
        created_user = await register_user_use_case.execute(
            name=user.name, email=user.email, password=user.password
        )
        return UserResponse(
            id=created_user.id,
            name=created_user.name.value,
            email=created_user.email.value,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.get("/me", response_model=UserResponse)
async def read_user_me(current_user: User = Depends(get_current_user)):
    return UserResponse(
        id=current_user.id, name=current_user.name.value, email=current_user.email.value
    )


@user_router.get("/users", response_model=UserResponse)
async def read_user_by_email(
    email: str, factory: UseCaseFactory = Depends(get_use_case_factory)
):
    find_user_use_case = factory.create_find_user_by_email()
    user = await find_user_use_case.execute(email=email)
    if user:
        return UserResponse(id=user.id, name=user.name.value, email=user.email.value)
    else:
        raise HTTPException(status_code=400, detail=str("User not found!"))
