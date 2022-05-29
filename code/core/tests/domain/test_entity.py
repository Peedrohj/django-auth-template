# Utils
import unittest
from datetime import datetime
from dataclasses import FrozenInstanceError, is_dataclass


# Entities
from core.domain.entity import Entity

class TestBaseEntity(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Entity))

    def test_if_id_is_being_generated(self):
        entity = Entity()
        self.assertIsNotNone(entity.id)

    def test_if_created_at_is_being_generated(self):
        entity = Entity()
        self.assertIsNotNone(entity.created_at)

    def test_if_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = Entity()
            value_object.id = "Teste"












            
