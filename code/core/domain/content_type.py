# Utils
from dataclasses import dataclass
# from django.contrib.auth.models
# Entities
from core.domain.entity import BaseEntityId


@dataclass(kw_only=True, frozen=True, slots=True)
class ContentType(BaseEntityId):
    app_label: str
    model: str
