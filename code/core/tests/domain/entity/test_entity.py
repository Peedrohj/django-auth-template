# Utils
import unittest
from dataclasses import FrozenInstanceError, is_dataclass
from datetime import datetime

# Entities
from core.domain.entity.base import BaseEntityId, Entity


class TestBaseEntityID(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(BaseEntityId))

    def test_if_id_is_being_generated(self):
        entity = Entity()
        self.assertIsNotNone(entity.id)

    def test_if_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = Entity()
            value_object.id = "Teste"


class TestBaseEntity(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Entity))

    def test_if_created_at_is_being_generated(self):
        entity = Entity()
        self.assertIsNotNone(entity.created_at)
        self.assertIsInstance(entity.created_at, datetime)

    def test_if_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = Entity()
            value_object.created_at = "Teste"
