# Utils
from dataclasses import dataclass

# Entities
from core.domain.entities import Permission

# Repositories
from core.domain.repositories import PermissionRepository


@dataclass(slots=True)
class CreatePermission:
    permission_repository: PermissionRepository

    def execute(self, permission: Permission) -> Permission:
        return self.permission_repository.insert(permission=permission)
