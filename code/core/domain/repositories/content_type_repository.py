# Utils
from abc import ABC, abstractmethod
from typing import Dict, List

# Entities
from core.domain.entities import ContentType
from core.domain.value_objects import UniqueEntityId


class ContentTypeRepository(ABC):
    @abstractmethod
    def insert(self, content_type: ContentType) -> ContentType:
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, content_type_id: str | UniqueEntityId) -> ContentType:
        raise NotImplementedError()

    @abstractmethod
    def find_all(self, filters: Dict = None) -> List[ContentType]:
        raise NotImplementedError()

    @abstractmethod
    def update(self, content_type_id: str | UniqueEntityId, content_type: ContentType) -> ContentType:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, content_type_id: str | UniqueEntityId) -> None:
        raise NotImplementedError()
