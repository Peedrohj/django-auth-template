# Utils
from abc import ABC, abstractmethod
from typing import Dict, List

# Entities
from core.domain.entity.permission_group import PermissionGroup
from core.domain.value_objects import UniqueEntityId


class PermissionGoupRepository(ABC):
    @abstractmethod
    def insert(self, group: PermissionGroup) -> PermissionGroup:
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, group_id: str | UniqueEntityId) -> PermissionGroup:
        raise NotImplementedError()

    @abstractmethod
    def find_all(self, filters: Dict = None) -> List[PermissionGroup]:
        raise NotImplementedError()

    @abstractmethod
    def update(self, group_id: str | UniqueEntityId, group: PermissionGroup) -> PermissionGroup:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, group_id: str | UniqueEntityId) -> None:
        raise NotImplementedError()
