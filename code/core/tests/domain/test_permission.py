# Utils
import unittest
from dataclasses import FrozenInstanceError, is_dataclass
from os import name
from core.domain.exceptions import InvalidContentTypeException
# Entities
from core.domain.permission import ContentType, Permission


class TestPermission(unittest.TestCase):
    def setUp(self) -> None:
        self.content_type = ContentType(app_label="Test", model="test")
        self.permission_props = {
            "name": "test",
            "codename": "test",
            "content_type": self.content_type
        }

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Permission))

    def test_create_permission(self):
        permission = Permission(**self.permission_props)
        self.assertEqual(permission.name, self.permission_props["name"])
        self.assertEqual(permission.codename, self.permission_props["codename"])
        self.assertIsNotNone(permission.id)

    def test_cannot_create_permission_with_invalid_content_type(self):
        with self.assertRaises(InvalidContentTypeException):
            invalid_permission_props = {
                "name": "test",
                "codename": "test",
                "content_type": "test"
            }
            permission = Permission(**invalid_permission_props)
            permission.id = "Teste"

    def test_if_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            permission = Permission(**self.permission_props)
            permission.id = "Teste"
