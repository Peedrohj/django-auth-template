# Utils
import unittest

# Entities
from core.domain.entities import ContentType, Permission

# Repositories
from core.infrastructure.repositories.in_memory.permission_repository import \
    InMemoryPermissionRepository


class TestPermissionRepository(unittest.TestCase):
    permission_repo: InMemoryPermissionRepository

    def setUp(self) -> None:
        self.permission_repo = InMemoryPermissionRepository()
        self.content_type = ContentType(app_label="Test", model="Test")
        self.permission_props = {
            "name": "Test",
            "codename": "Test",
            "content_type": self.content_type
        }
        self.permission = Permission(**self.permission_props)

    def test_insert_permission(self):
        self.permission_repo.insert(permission=self.permission)
        self.assertEqual(self.permission_repo.db[0], self.permission)

    def test_find_by_id(self):
        self.permission_repo.insert(permission=self.permission)
        permission = self.permission_repo.find_by_id(
            permission_id=self.permission.id)
        self.assertEqual(permission, self.permission)

    def test_find_all(self):
        self.permission_repo.insert(permission=self.permission)
        self.assertEqual(self.permission_repo.db, [self.permission])

    def test_update_permission(self):
        permission_props = {**self.permission_props, "name": "Test 1"}
        expected_data = {**self.permission.to_dict(), "name": "Test 1"}

        new_permission = Permission(**permission_props)
        self.permission_repo.insert(permission=self.permission)
        self.permission_repo.update(
            permission_id=self.permission.id, permission=new_permission)
        permission = self.permission_repo.find_by_id(
            permission_id=self.permission.id)

        self.assertEqual(
            permission.to_dict(), expected_data)

    def test_delete_permission(self):
        self.permission_repo.insert(permission=self.permission)
        self.permission_repo.delete(permission_id=self.permission.id)
        self.assertEqual(self.permission_repo.db, [])
