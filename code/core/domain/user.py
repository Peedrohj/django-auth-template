# Utils
from dataclasses import dataclass

# Entities
from core.domain.entity import Entity

@dataclass(kw_only=True, frozen=True, slots=True) 
class User(Entity):
    name: str
    is_active: bool

    def update(self, name: str):
        self._set('name', name)

    def activate(self):
        self._set('is_active', True)

    def deactivate(self):
        self._set('is_active', False)