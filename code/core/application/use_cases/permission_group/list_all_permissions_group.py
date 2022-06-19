# Utils
from dataclasses import dataclass
from typing import Dict, List

# Entites
from core.domain.entities import PermissionGroup
from core.domain.value_objects import UniqueEntityId

# Repositories
from core.domain.repositories import PermissionGroupRepository


@dataclass(slots=True)
class ListAllPermissionsGroup:
    permission_group_repository: PermissionGroupRepository

    def execute(self, group_id: str | UniqueEntityId = None, filters: Dict = None) -> List[PermissionGroup]:
        if group_id is not None:
            return self.permission_group_repository.find_by_id(group_id=group_id)

        return self.permission_group_repository.find_all(filters=filters)
