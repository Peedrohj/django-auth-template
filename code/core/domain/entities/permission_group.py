# Utils
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List

# Entities
from core.domain.entities import BaseEntityId, Permission
from core.domain.exceptions import InvalidPermissionException

if TYPE_CHECKING:
    from core.domain.entities import User


@dataclass(kw_only=True, frozen=True, slots=True)
class PermissionGroup(BaseEntityId):
    name: str
    permissions: List[Permission] = field(default_factory=list)

    def __post_init__(self):
        self.__validate()

    def __validate(self):
        for permission in self.permissions:
            if not isinstance(permission, Permission):
                raise InvalidPermissionException()
