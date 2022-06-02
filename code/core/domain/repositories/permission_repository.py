# Utils
from abc import ABC, abstractmethod
from typing import Dict, List

# Entities
from core.domain.entity.permission import Permission
from core.domain.value_objects import UniqueEntityId


class PermissionRepository(ABC):
    @abstractmethod
    def insert(self, permission: Permission) -> Permission:
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, permission_id: str | UniqueEntityId) -> Permission:
        raise NotImplementedError()

    @abstractmethod
    def find_all(self, filters: Dict = None) -> List[Permission]:
        raise NotImplementedError()

    @abstractmethod
    def update(self, permission: Permission) -> Permission:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, permission_id: str | UniqueEntityId) -> None:
        raise NotImplementedError()
