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

    def test_if_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            user = User(**self.user_props)
            user.id = "Teste"
