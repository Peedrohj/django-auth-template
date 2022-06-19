# Utils
from dataclasses import dataclass
from typing import Dict, List

# Entites
from core.domain.entities import User
from core.domain.value_objects import UniqueEntityId

# Repositories
from core.domain.repositories import UserRepository


@dataclass(slots=True)
class ListAllPermissionsGroup:
    user_repository: UserRepository

    def execute(self, user_id: str | UniqueEntityId = None, filters: Dict = None) -> List[User]:
        if user_id is not None:
            return self.user_repository.find_by_id(user_id=user_id)

        return self.user_repository.find_all(filters=filters)
