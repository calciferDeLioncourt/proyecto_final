from datetime import datetime, timedelta, timezone

import jwt

from proyecto_final.core.settings import settings

# from proyecto_final.config.security import (
#     ACCESS_TOKEN_EXPIRE_MINUTES,
#     ALGORITHM,
#     SECRET_KEY,
# )


class JWTService:

    @staticmethod
    def create_access_token(
        data: dict,
    ) -> str:

        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.access_token_expire_minutes
        )

        to_encode.update(
            {
                "exp": expire,
            }
        )

        return jwt.encode(
            to_encode,
            settings.jwt_secret_key,
            algorithm=settings.jwt_algorithm,
        )

    @staticmethod
    def decode_token(
        token: str,
    ) -> dict:

        return jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm],
        )
