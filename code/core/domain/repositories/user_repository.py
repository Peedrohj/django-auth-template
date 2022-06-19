# Utils
from abc import ABC, abstractmethod
from typing import Dict, List

# Entities
from core.domain.entities import User
from core.domain.value_objects import UniqueEntityId


class UserRepository(ABC):
    @abstractmethod
    def insert(self, user: User) -> User:
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, user_id: str | UniqueEntityId) -> User:
        raise NotImplementedError()

    @abstractmethod
    def find_all(self, filters: Dict = None) -> List[User]:
        raise NotImplementedError()

    @abstractmethod
    def update(self, user_id: str | UniqueEntityId, user: User) -> User:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, user_id: str | UniqueEntityId) -> None:
        raise NotImplementedError()
