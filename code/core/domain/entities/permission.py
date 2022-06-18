# Utils
from dataclasses import dataclass

# Entities
from core.domain.entities import BaseEntityId, ContentType
from core.domain.exceptions import InvalidContentTypeException


@dataclass(kw_only=True, frozen=True, slots=True)
class Permission(BaseEntityId):
    name: str
    content_type: ContentType
    codename: str

    def __post_init__(self):
        self.__validate()

    def __validate(self):
        if not isinstance(self.content_type, ContentType):
            raise InvalidContentTypeException()
