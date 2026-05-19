from proyecto_final.application.services.password_service import (
    PasswordService,
)
from proyecto_final.domain.entities.user import User


class InMemoryUserRepository:

    def __init__(self):

        self.users = {
            "admin": User(
                username="admin",
                hashed_password=(PasswordService.hash_password("123456")),
            )
        }

    def get_by_username(
        self,
        username: str,
    ) -> User | None:

        return self.users.get(username)
