from fastapi import APIRouter, Depends, HTTPException

from api.dependencies import get_use_case_factory, get_current_user
from api.schemas.user_schemas import UserCreate, UserResponse
from core.factories.use_case_factory import UseCaseFactory

user_router = APIRouter()


@user_router.post("/users", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    try:
        register_user = factory.create_register_user()
        created = await register_user.execute(
            email=user.email,
            password=user.password,
        )
        return UserResponse.from_entity(created)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.get("/me", response_model=UserResponse)
async def get_me(current_user = Depends(get_current_user)):
    return UserResponse.from_entity(current_user)


@user_router.get("/users/by-email", response_model=UserResponse)
async def get_user_by_email(
    email: str,
    factory: UseCaseFactory = Depends(get_use_case_factory),
):
    find_user = factory.create_find_user_by_email()
    user = await find_user.execute(email=email)

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return UserResponse.from_entity(user)
