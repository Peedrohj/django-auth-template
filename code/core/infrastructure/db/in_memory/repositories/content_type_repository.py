# Utils
from dataclasses import dataclass, field
from typing import List, Dict

# Entities
from core.domain.value_objects import UniqueEntityId
from core.domain.entities.content_type import ContentType

# Repositories
from core.domain.repositories import ContentTypeRepository
from core.infrastructure.db.in_memory.repositories.base_repository import InMemoryBaseEntityRepository


@dataclass(slots=True)
class InMemoryContentTypeRepository(ContentTypeRepository, InMemoryBaseEntityRepository):
    db: List[ContentType] = field(default_factory=list)

    def insert(self, content_type: ContentType) -> ContentType:
        self.db.append(content_type)
        return content_type

    def find_by_id(self, content_type_id: str | UniqueEntityId) -> ContentType:
        return self._get(str(content_type_id))

    def find_all(self, filters: Dict = None) -> List[ContentType]:
        return self.db

    def update(self, content_type_id: str | UniqueEntityId, content_type: ContentType) -> ContentType:
        old_content_type: ContentType = self._get(str(content_type_id))
        index = self.db.index(old_content_type)
        new_content_type_data = {
            **content_type.to_dict(),
            "id": content_type_id,
        }

        new_content_type = ContentType(**new_content_type_data)
        self.db[index] = new_content_type
        return new_content_type

    def delete(self, content_type_id: str | UniqueEntityId) -> None:
        old_content_type = self._get(str(content_type_id))
        self.db.remove(old_content_type)
