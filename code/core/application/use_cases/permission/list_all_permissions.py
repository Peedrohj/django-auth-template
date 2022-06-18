# Utils
from dataclasses import dataclass
from typing import List

# Entites
from core.domain.entity import Permission

# Repositories
from core.domain.repositories.permission_repository import PermissionRepository


@dataclass(slots=True)
class ListAllPermissions:
    permission_repository: PermissionRepository

    def execute(self) -> List[Permission]:
        return self.permission_repository.find_all()
