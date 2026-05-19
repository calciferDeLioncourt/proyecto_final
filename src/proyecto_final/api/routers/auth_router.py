from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from proyecto_final.api.schemas.auth_schema import (
    LoginSchema,
    TokenResponseSchema,
)
from proyecto_final.application.services.jwt_service import JWTService
from proyecto_final.application.services.password_service import (
    PasswordService,
)
from proyecto_final.infrastructure.repositories.in_memory_user_repository import (
    InMemoryUserRepository,
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post(
    "/login",
    response_model=TokenResponseSchema,
)
def login(
    schema: LoginSchema,
):

    repository = InMemoryUserRepository()

    user = repository.get_by_username(schema.username)

    if not user:

        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    is_valid = PasswordService.verify_password(
        schema.password,
        user.hashed_password,
    )

    if not is_valid:

        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token = JWTService.create_access_token(
        {
            "sub": user.username,
        }
    )

    return TokenResponseSchema(
        access_token=token,
        token_type="bearer",
    )
