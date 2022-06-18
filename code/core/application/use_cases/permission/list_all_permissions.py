# Utils
from dataclasses import dataclass
from typing import Dict, List

# Entites
from core.domain.entities import Permission
from core.domain.value_objects import UniqueEntityId

# Repositories
from core.domain.repositories import PermissionRepository


@dataclass(slots=True)
class ListAllPermissions:
    permission_repository: PermissionRepository

    def execute(self, permission_id: str | UniqueEntityId = None, filters: Dict = None) -> List[Permission]:
        if permission_id is not None:
            return self.permission_repository.find_by_id(permission_id=permission_id)

        return self.permission_repository.find_all(filters=filters)
