# Utils
from dataclasses import dataclass

# Entities
from core.domain.entities import Permission
from core.domain.value_objects.unique_entity_id import UniqueEntityId

# Repositories
from core.domain.repositories import PermissionRepository

# Exceptions
from core.domain.exceptions import InvalidUUidException


@dataclass(slots=True)
class UpdatePermission:
    permission_repository: PermissionRepository

    def execute(self, permission_id: str | UniqueEntityId, permission: Permission) -> Permission:
        if not permission_id:
            raise InvalidUUidException()

        return self.permission_repository.update(permission_id=permission_id, permission=permission)
