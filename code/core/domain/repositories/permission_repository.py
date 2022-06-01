# Utils
from abc import ABC
from typing import Dict, List

# Entities
from core.domain.entity.permission import Permission


class PermissionRepository(ABC):
    def find(self) -> Permission:
        raise NotImplementedError()

    def find_all(self, filters: Dict = None) -> List[Permission]:
        raise NotImplementedError()

    def save(self, permission: Permission) -> Permission:
        raise NotImplementedError()

    def delete(self, permission_id: str) -> None:
        raise NotImplementedError()
