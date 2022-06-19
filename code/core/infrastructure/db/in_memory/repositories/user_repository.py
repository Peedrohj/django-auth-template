# Utils
from dataclasses import dataclass, field
from typing import List, Dict

# Entities
from core.domain.value_objects import UniqueEntityId
from core.domain.entities.user import User

# Repositories
from core.domain.repositories import UserRepository
from core.infrastructure.db.in_memory.repositories.base_repository import InMemoryBaseEntityRepository


@dataclass(slots=True)
class InMemoryUserRepository(UserRepository, InMemoryBaseEntityRepository):
    db: List[User] = field(default_factory=list)

    def insert(self, user: User) -> User:
        self.db.append(user)
        return user

    def find_by_id(self, user_id: str | UniqueEntityId) -> User:
        return self._get(str(user_id))

    def find_all(self, filters: Dict = None) -> List[User]:
        return self.db

    def update(self, user_id: str | UniqueEntityId, user: User) -> User:
        old_user: User = self._get(str(user_id))
        index = self.db.index(old_user)
        new_user_data = {
            **user.to_dict(),
            "id": user_id,
            "permissions": user.permissions,
            "permissions_groups": user.permissions_groups,
        }

        new_user = User(**new_user_data)
        self.db[index] = new_user
        return new_user

    def delete(self, user_id: str | UniqueEntityId) -> None:
        old_user = self._get(str(user_id))
        self.db.remove(old_user)
