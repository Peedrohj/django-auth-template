# Utils
from dataclasses import dataclass

# Entities
from core.domain.value_objects.unique_entity_id import UniqueEntityId

# Repositories
from core.domain.repositories import PermissionRepository

# Exceptions
from core.domain.exceptions import InvalidUUidException


@dataclass(slots=True)
class DeletePermission:
    permission_repository: PermissionRepository

    def execute(self, permission_id: str | UniqueEntityId):
        if not permission_id:
            raise InvalidUUidException()

        return self.permission_repository.delete(permission_id=id)
