# Utils
from typing import List, Dict

# Entities
from core.domain.value_objects import UniqueEntityId
from core.domain.entity.permission import Permission

# Repositories
from core.domain.repositories.permission_repository import PermissionRepository
from core.infrastructure.repositories.in_memory.base_repository import InMemoryBaseEntityRepository


class InMemoryPermissionRepository(PermissionRepository, InMemoryBaseEntityRepository):
    def insert(self, permission: Permission) -> Permission:
        self.db.append(permission)
        return permission

    def find_by_id(self, permission_id: str | UniqueEntityId) -> Permission:
        return self._get(str(permission_id))

    def find_all(self, filters: Dict = None) -> List[Permission]:
        return self.db

    def update(self, permission_id: str | UniqueEntityId, permission: Permission) -> Permission:
        old_permission: Permission = self._get(str(permission_id))
        index = self.db.index(old_permission)

        new_permission_data = {**permission.to_dict(), "id": permission_id, "content_type": permission.content_type}
        new_permission = Permission(**new_permission_data)
        self.db[index] = new_permission
        return new_permission

    def delete(self, permission_id: str | UniqueEntityId) -> None:
        old_permission = self._get(str(permission_id))
        self.db.remove(old_permission)
