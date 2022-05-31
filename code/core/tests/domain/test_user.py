# Utils
import unittest
from dataclasses import FrozenInstanceError, is_dataclass
from datetime import datetime

# Entities
from core.domain.user import User
from core.domain.content_type import ContentType
from core.domain.exceptions import InvalidPermissionException, InvalidGroupException
from core.domain.permission import Permission
from core.domain.permission_group import PermissionGroup


class TestPermissionGroup(unittest.TestCase):
    def setUp(self) -> None:
        self.permission = Permission(name="Test", codename="Test", content_type=ContentType(
            app_label="Test", model="Test"))
        self.permissions_groups = PermissionGroup(
            name="Test", permissions=[self.permission])
        self.user_props = {
            "email": "test_email@email.com.br",
            "first_name": "Test",
            "last_name": "Test",
            "is_active": True,
            "is_superuser": True,
            "is_staff": False,
            "date_joined": datetime.now(),
            "permissions": [self.permission],
            "permissions_groups": [self.permissions_groups],
        }

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(User))

    def test_if_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            user = User(**self.user_props)
            user.id = "Teste"

    def test_create_user(self):
        user = User(**self.user_props)
        expected_data = {
            **self.user_props,
            "permissions": [self.permission.to_dict()],
            "permissions_groups": [self.permissions_groups.to_dict()],
        }

        self.assertIsNotNone(user.id)
        self.assertDictContainsSubset(expected_data, user.to_dict())

    def test_create_user_without_permissions(self):
        user_props = {**self.user_props, "permissions": []}
        user = User(**user_props)
        expected_data = {
            **user_props,
            "permissions_groups": [self.permissions_groups.to_dict()],
        }

        self.assertIsNotNone(user.id)
        self.assertDictContainsSubset(expected_data, user.to_dict())

    def test_create_user_without_permissions_groups(self):
        user_props = {**self.user_props, "permissions_groups": []}
        user = User(**user_props)
        expected_data = {
            **user_props,
            "permissions": [self.permission.to_dict()],
        }

        self.assertIsNotNone(user.id)
        self.assertDictContainsSubset(expected_data, user.to_dict())

    def test_deactivate_user(self):
        user = User(**self.user_props)
        user.deactivate()

        self.assertFalse(user.is_active)

    def test_activate_user(self):
        user_props = {**self.user_props, "is_active": False}
        user = User(**user_props)
        user.activate()

        self.assertTrue(user.is_active)

    def test_add_permissions(self):
        user = User(**self.user_props)
        user_permission = Permission(name="Test 1", codename="Test 1", content_type=ContentType(
            app_label="Test", model="Test"))
        user.add_permission(permission=user_permission)

        self.assertEqual(len(user.permissions), 2)
        self.assertEqual([self.permission, user_permission], user.permissions)

    def test_remove_permissions(self):
        user = User(**self.user_props)
        user.remove_permission(permission_id=self.permission.id)

        self.assertEqual(len(user.permissions), 0)
        self.assertEqual([], user.permissions)

    def test_add_permissions_groups(self):
        user = User(**self.user_props)
        permissions_goup = PermissionGroup(
            name="Test 1", permissions=[self.permission])
        user.add_permission_group(group=permissions_goup)

        self.assertEqual(len(user.permissions_groups), 2)
        self.assertEqual([self.permissions_groups, permissions_goup], user.permissions_groups)

    def test_remove_permissions_groups(self):
        user = User(**self.user_props)
        user.remove_permission_group(group_id=self.permissions_groups.id)

        self.assertEqual(len(user.permissions_groups), 0)
        self.assertEqual([], user.permissions_groups)
