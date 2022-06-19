# Utils
from dataclasses import dataclass

# Entities
from core.domain.value_objects.unique_entity_id import UniqueEntityId

# Repositories
from core.domain.repositories import PermissionGroupRepository

# Exceptions
from core.domain.exceptions import InvalidUUidException


@dataclass(slots=True)
class DeletePermissionGroup:
    permission_group_repository: PermissionGroupRepository

    def execute(self, group_id: str | UniqueEntityId):
        if not group_id:
            raise InvalidUUidException()

        return self.permission_group_repository.delete(group_id=id)
