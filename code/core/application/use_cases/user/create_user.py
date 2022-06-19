# Utils
from dataclasses import dataclass

# Entities
from core.domain.entities import User

# Repositories
from core.domain.repositories import UserRepository


@dataclass(slots=True)
class CreateUser:
    user_repository: UserRepository

    def execute(self, user: User) -> User:
        return self.user_repository.insert(user=user)
