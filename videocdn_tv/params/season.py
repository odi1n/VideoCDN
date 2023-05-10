from dataclasses import dataclass
from typing import Optional

from videocdn_tv.params.base import BaseParams


@dataclass
class ParamsSeason(BaseParams):
    tv_series_id: Optional[int] = None

    def as_dict(self) -> dict:
        return {
            "tv_series_id": self.tv_series_id,
            **super().as_dict(),
        }
