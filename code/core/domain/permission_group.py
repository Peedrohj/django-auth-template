# Utils
from dataclasses import dataclass, field
from typing import List
from core.domain.exceptions import InvalidPermissionsException

# Entities
from core.domain.entity import BaseEntityId
from core.domain.permission import Permission

@dataclass(kw_only=True, frozen=True, slots=True)
class PermissionGroup(BaseEntityId):
    name: str
    permissions: List[Permission] = field(default_factory=lambda: list())

    def __post_init__(self):
        self.__validate()

    def __validate(self):
        for permission in self.permissions:
            if not isinstance(permission, Permission):
                raise InvalidPermissionsException()
