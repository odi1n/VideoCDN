from dataclasses import dataclass
from typing import Optional

from videocdn_tv.params.base import BaseParams
from videocdn_tv.type.field import Field


@dataclass
class ParamsContent(BaseParams):
    query: Optional[str] = None
    field: Optional[Field] = None
    translation: Optional[int] = None
    year: Optional[int] = None

    def as_dict(self) -> dict:
        return {
            "field": self.field.value if self.field else None,
            "query": self.query,
            "translation": self.translation,
            "year": self.year,
            **super().as_dict(),
        }
