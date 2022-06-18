# Utils
from abc import ABC
from typing import List, TypeVar

# Entities
from core.domain.entities import BaseEntityId, Entity as DomainEntity
from core.domain.value_objects import UniqueEntityId

# Repositories
from core.domain.exceptions import NotFoundException

BaseEntity = TypeVar('BaseEntity', bound=BaseEntityId)
Entity = TypeVar('Entity', bound=DomainEntity)


class InMemoryBaseEntityRepository(ABC):
    db: List[BaseEntity] = []

    def _get(self, entity_id: str | UniqueEntityId) -> BaseEntity:
        entity = next(filter(lambda i: i.id == entity_id, self.db), None)
        if not entity:
            raise NotFoundException(f"Entity not found using ID '{entity_id}'")
        return entity
