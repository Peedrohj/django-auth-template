# Utils
from dataclasses import dataclass

# Entities
from core.domain.content_type import ContentType
from core.domain.entity import BaseEntityId

@dataclass(kw_only=True, frozen=True, slots=True)
class Permision(BaseEntityId):
    name: str
    content_type: ContentType
    codename: str
