from datetime import datetime, timedelta, timezone

import jwt

from proyecto_final.config.security import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    SECRET_KEY,
)


class JWTService:

    @staticmethod
    def create_access_token(
        data: dict,
    ) -> str:

        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

        to_encode.update(
            {
                "exp": expire,
            }
        )

        return jwt.encode(
            to_encode,
            SECRET_KEY,
            algorithm=ALGORITHM,
        )

    @staticmethod
    def decode_token(
        token: str,
    ) -> dict:

        return jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
