# Utils
import unittest
from dataclasses import FrozenInstanceError, is_dataclass

# Entities
from core.domain.entities import ContentType, Permission, PermissionGroup
from core.domain.exceptions import InvalidPermissionException


class TestPermissionGroup(unittest.TestCase):
    def setUp(self) -> None:
        self.permission = Permission(name="Test", codename="Test", content_type=ContentType(
            app_label="Test", model="Test"))
        self.permission_group_props = {
            "name": "test",
            "permissions": [self.permission]
        }

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(PermissionGroup))

    def test_create_permission_group(self):
        permission_group = PermissionGroup(**self.permission_group_props)
        self.assertEqual(permission_group.name,
                         self.permission_group_props["name"])
        self.assertEqual(permission_group.permissions,
                         self.permission_group_props["permissions"])
        self.assertIsNotNone(permission_group.id)

    def test_cannot_create_permission_group_with_invalid_permissions(self):
        with self.assertRaises(InvalidPermissionException):
            invalid_permission_group_props = {
                "name": "test",
                "permissions": ["test"]
            }
            permission_group = PermissionGroup(
                **invalid_permission_group_props)
            permission_group.id = "Teste"

    def test_if_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            permission_group = PermissionGroup(**self.permission_group_props)
            permission_group.id = "Teste"
