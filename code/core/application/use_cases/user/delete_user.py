# Utils
from dataclasses import dataclass

# Entities
from core.domain.value_objects.unique_entity_id import UniqueEntityId

# Repositories
from core.domain.repositories import UserRepository

# Exceptions
from core.domain.exceptions import InvalidUUidException


@dataclass(slots=True)
class DeleteUser:
    user_repository: UserRepository

    def execute(self, user_id: str | UniqueEntityId):
        if not user_id:
            raise InvalidUUidException()

        return self.user_repository.delete(user_id=id)
