# Utils
from dataclasses import dataclass
from datetime import datetime
from typing import List

# Entities
from core.domain.entity import Entity, Permission, PermissionGroup
from core.domain.exceptions import (InvalidGroupException,
                                    InvalidPermissionException)


@dataclass(kw_only=True, frozen=True, slots=True)
class User(Entity):
    email: str
    first_name: str
    last_name: str
    is_active: bool
    is_superuser: bool
    is_staff: bool
    date_joined: datetime

    permissions: List[Permission]
    permissions_groups: List[PermissionGroup]

    @property
    def full_name(self):
        return f"${self.first_name} ${self.last_name}".strip()

    @property
    def short_name(self):
        return self.first_name

    def __post_init__(self):
        self.__validate()

    def activate(self):
        self._set('is_active', True)

    def deactivate(self):
        self._set('is_active', False)

    def add_permission(self, permission: Permission):
        if not isinstance(permission, Permission):
            raise InvalidPermissionException()
        permission_list = self.permissions
        permission_list.append(permission)
        self._set('permissions', permission_list)

    def add_permission_group(self, group: PermissionGroup):
        if not isinstance(group, PermissionGroup):
            raise InvalidGroupException()
        permissions_groups_list = self.permissions_groups
        permissions_groups_list.append(group)
        self._set('permissions_groups', permissions_groups_list)

    def remove_permission(self, permission_id: str):
        permission_list = list(filter(
            lambda permission: permission.id != permission_id, self.permissions))
        self._set('permissions', permission_list)

    def remove_permission_group(self, group_id: str):
        permissions_groups_list = list(filter(
            lambda group: group.id != group_id, self.permissions_groups))
        self._set('permissions_groups', permissions_groups_list)

    def __validate(self):
        for permission in self.permissions:
            if not isinstance(permission, Permission):
                raise InvalidPermissionException()

        for group in self.permissions_groups:
            if not isinstance(group, PermissionGroup):
                raise InvalidGroupException()
