from dataclasses import dataclass
from typing import Optional

from videocdn_tv.params.base import BaseParams
from videocdn_tv.type.field import Field


@dataclass
class ParamsEpisode(BaseParams):
    tv_series_id: Optional[int] = None
    season_id: Optional[int] = None
    field: Optional[Field] = None
    query: Optional[str] = None

    def as_dict(self) -> dict:
        return {
            "tv_series_id": self.tv_series_id,
            "season_id": self.season_id,
            "field": self.field.value if self.field else None,
            "query": self.query,
            **super().as_dict(),
        }
