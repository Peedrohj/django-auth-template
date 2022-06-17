# Utils
import json
import uuid
from abc import ABC
from dataclasses import dataclass, field

from core.domain.exceptions import InvalidUUidException
from core.domain.value_objects import ValueObject


@dataclass(frozen=True, slots=True)
class UniqueEntityId(ValueObject):

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    def __post_init__(self):
        id_value = str(self.id) if isinstance(self.id, uuid.UUID) else self.id
        object.__setattr__(self, 'id', id_value)
        self.__validate()

    def __validate(self):
        try:
            uuid.UUID(self.id)
        except ValueError as ex:
            raise InvalidUUidException() from ex
