# Utils
import unittest
import uuid
from abc import ABC
from dataclasses import FrozenInstanceError, is_dataclass
from unittest.mock import patch

# Domain
from core.domain.exceptions import InvalidUUidException
from core.domain.value_objects import UniqueEntityId, ValueObject


class TestValueObject(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_if_is_a_abstract_class(self):
        self.assertIsInstance(ValueObject(), ABC)


class TestUniqueEntityId(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_throw_exception_when_uuid_is_invalid(self):
        with patch.object(
            UniqueEntityId,
            "_UniqueEntityId__validate",
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            with self.assertRaises(InvalidUUidException) as assert_error:
                UniqueEntityId(id="fake id")
            mock_validate.assert_called_once()
            self.assertEqual(
                assert_error.exception.args[0], "ID must be a valid UUID")

    def test_if_accept_uuid_passed_in_constructor(self):
        uuid_example = uuid.uuid4()
        value_object = UniqueEntityId(id=uuid_example)
        self.assertEqual(value_object.id, str(uuid_example))

    def test_if_id_is_created_in_constructor(self):
        value_object = UniqueEntityId()
        uuid.UUID(value_object.id)

    def test_if_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = UniqueEntityId()
            value_object.id = "Fake Id"
