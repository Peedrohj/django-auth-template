# Utils
import unittest
from dataclasses import FrozenInstanceError, is_dataclass

# Entities
from core.domain.entity.content_type import ContentType


class TestContentType(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(ContentType))

    def test_create_content_type(self):
        content_type_props = {
            "app_label": "test_app",
            "model": "test",
        }

        content_type = ContentType(**content_type_props)

        self.assertEqual(content_type.app_label,
                         content_type_props["app_label"])
        self.assertEqual(content_type.model, content_type_props["model"])
        self.assertIsNotNone(content_type.id)

    def test_if_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            content_type_props = {
                "app_label": "test_app",
                "model": "test",
            }

            content_type = ContentType(**content_type_props)
            content_type.id = "Teste"
