# Utils
from dataclasses import dataclass
from typing import List, Dict

# Entities
from core.domain.value_objects import UniqueEntityId
from core.domain.entity.permission_group import PermissionGroup

# Repositories
from core.domain.repositories.permission_group_repository import PermissionGoupRepository
from core.infrastructure.repositories.in_memory.base_repository import InMemoryBaseEntityRepository

@dataclass(slots=True)
class InMemoryPermissionGoupRepository(PermissionGoupRepository, InMemoryBaseEntityRepository):
    def insert(self, group: PermissionGroup) -> PermissionGroup:
        self.db.append(group)
        return group

    def find_by_id(self, group_id: str | UniqueEntityId) -> PermissionGroup:
        return self._get(str(group_id))

    def find_all(self, filters: Dict = None) -> List[PermissionGroup]:
        return self.db

    def update(self, group_id: str | UniqueEntityId, group: PermissionGroup) -> PermissionGroup:
        old_group: PermissionGroup = self._get(str(group_id))
        index = self.db.index(old_group)
        new_group_data = {
            **group.to_dict(),
            "id": group_id,
            "permissions": group.permissions
        }

        new_group = PermissionGroup(**new_group_data)
        self.db[index] = new_group
        return new_group

    def delete(self, group_id: str | UniqueEntityId) -> None:
        old_group = self._get(str(group_id))
        self.db.remove(old_group)
