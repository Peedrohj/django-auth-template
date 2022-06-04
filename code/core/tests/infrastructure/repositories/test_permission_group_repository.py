# Utils
import unittest

# Entities
from core.domain.entity.content_type import ContentType
from core.domain.entity.permission import Permission
from core.domain.entity.permission_group import PermissionGroup

# Repositories
from core.infrastructure.repositories.in_memory.permission_group_repository import InMemoryPermissionGoupRepository


class TestPermissionRepository(unittest.TestCase):
    permission_group_repo: InMemoryPermissionGoupRepository 

    def setUp(self) -> None:
        self.permission_group_repo = InMemoryPermissionGoupRepository()
        self.group = Permission(name="Test", codename="Test", content_type=ContentType(
            app_label="Test", model="Test"))
        self.group_props = {
            "name": "test",
            "permissions": [self.group]
        }
        self.group = PermissionGroup(**self.group_props)

    def test_insert_permission(self):
        self.permission_group_repo.insert(group=self.group)
        self.assertEqual(self.permission_group_repo.db[0], self.group)

    def test_find_by_id(self):
        self.permission_group_repo.insert(group=self.group)
        permission = self.permission_group_repo.find_by_id(
            group_id=self.group.id)
        self.assertEqual(permission, self.group)

    def test_find_all(self):
        self.permission_group_repo.insert(group=self.group)
        self.assertEqual(self.permission_group_repo.db, [self.group])

    def test_update_permission(self):
        group_props = {**self.group_props, "name": "Test 1"}
        expected_data = {**self.group.to_dict(), "name": "Test 1"}

        new_group = PermissionGroup(**group_props)
        self.permission_group_repo.insert(group=self.group)
        self.permission_group_repo.update(
            group_id=self.group.id, group=new_group)
        permission = self.permission_group_repo.find_by_id(
            group_id=self.group.id)

        self.assertEqual(
            permission.to_dict(), expected_data)

    def test_delete_permission(self):
        self.permission_group_repo.insert(group=self.group)
        self.permission_group_repo.delete(group_id=self.group.id)
        self.assertEqual(self.permission_group_repo.db, [])
