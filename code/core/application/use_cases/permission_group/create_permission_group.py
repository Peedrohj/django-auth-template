# Utils
from dataclasses import dataclass

# Entities
from core.domain.entities import PermissionGroup

# Repositories
from core.domain.repositories import PermissionGroupRepository


@dataclass(slots=True)
class CreatePermissionGroup:
    permission_group_repository: PermissionGroupRepository

    def execute(self, group: PermissionGroup) -> PermissionGroup:
        return self.permission_group_repository.insert(group=group)
