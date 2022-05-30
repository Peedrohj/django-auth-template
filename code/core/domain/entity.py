# Utils
from abc import ABC
from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any, Optional

# Entities
from core.domain.value_objects import UniqueEntityId


@dataclass(frozen=True, slots=True)
class BaseEntityId(ABC):
    id: UniqueEntityId = field(
        default_factory=lambda: str(UniqueEntityId())
    )

    def to_dict(self):
        return asdict(self)

    def _set(self, name: str, value: Any):
        object.__setattr__(self, name, value)
        return self


@dataclass(frozen=True, slots=True)
class Entity(BaseEntityId, ABC):
    created_at: Optional[datetime] = field(
        default_factory=datetime.now
    )

    def __post_init__(self):
        if not self.created_at:
            self._set('created_at',  datetime.now())
