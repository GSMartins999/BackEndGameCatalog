from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import get_db
from core.domain.entities import User
from core.factories.use_case_factory import UseCaseFactory
from core.infra.sqlalchemy.user_repository import UserRepository
from core.infra.sqlalchemy.jogo_repository import JogoRepository
from core.security import ALGORITHM, SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/token",
    scheme_name="JWT"
)


def get_use_case_factory(
    db: AsyncSession = Depends(get_db),
) -> UseCaseFactory:
    user_repository = UserRepository(db)
    jogo_repository = JogoRepository(db)

    return UseCaseFactory(
        user_repository=user_repository,
        jogo_repository=jogo_repository,
    )


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    factory: UseCaseFactory = Depends(get_use_case_factory),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    find_user_by_email = factory.create_find_user_by_email()
    user = await find_user_by_email.execute(email=email)

    if user is None:
        raise credentials_exception

    return user
