# Utils
import unittest

# Entities
from core.domain.entities import ContentType

# Repositories
from core.infrastructure.db.in_memory.repositories import \
    InMemoryContentTypeRepository


class TestContentTypeRepository(unittest.TestCase):
    content_type_repo: InMemoryContentTypeRepository

    def setUp(self) -> None:
        self.content_type_repo = InMemoryContentTypeRepository()
        self.content_type_props = {
            "app_label": "Test",
            "model": "Test"
        }
        
        self.content_type= ContentType(**self.content_type_props)

    def test_insert_content_type(self):
        self.content_type_repo.insert(content_type=self.content_type)
        self.assertEqual(self.content_type_repo.db[0], self.content_type)

    def test_find_by_id(self):
        self.content_type_repo.insert(content_type=self.content_type)
        content_type = self.content_type_repo.find_by_id(
            content_type_id=self.content_type.id)
        self.assertEqual(content_type, self.content_type)

    def test_find_all(self):
        self.content_type_repo.insert(content_type=self.content_type)
        self.assertEqual(self.content_type_repo.db, [self.content_type])

    def test_update_content_type(self):
        content_type_props = {**self.content_type_props, "model": "Test 1"}
        expected_data = {**self.content_type.to_dict(), "model": "Test 1"}

        new_content_type = ContentType(**content_type_props)
        self.content_type_repo.insert(content_type=self.content_type)
        self.content_type_repo.update(
            content_type_id=self.content_type.id, content_type=new_content_type)
        content_type = self.content_type_repo.find_by_id(
            content_type_id=self.content_type.id)

        self.assertEqual(
            content_type.to_dict(), expected_data)

    def test_delete_content_type(self):
        self.content_type_repo.insert(content_type=self.content_type)
        self.content_type_repo.delete(content_type_id=self.content_type.id)
        self.assertEqual(self.content_type_repo.db, [])
