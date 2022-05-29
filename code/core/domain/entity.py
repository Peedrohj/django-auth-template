# Utils
from abc import ABC
from typing import Any, Optional
from datetime import datetime
from dataclasses import Field, dataclass, field, asdict
from core.domain.value_objects import UniqueEntityId


@dataclass(frozen=True, slots=True)
class Entity(ABC):
    id: UniqueEntityId = field(
        default_factory=lambda: str(UniqueEntityId())
    )
    created_at: Optional[datetime] = field(
        default_factory=datetime.now
    )

    def __post_init__(self):
        if not self.created_at:
            self._set('created_at',  datetime.now())

    def _set(self, name: str, value: Any):
        object.__setattr__(self, name, value)
        return self

    def to_dict(self):
        return asdict(self)
