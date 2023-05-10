from dataclasses import dataclass
from typing import Optional

from videocdn_tv.type.direction import Direction
from videocdn_tv.type.field import Field
from videocdn_tv.type.ordering import Ordering


@dataclass
class ParamsEpisode:
    tv_series_id: Optional[int] = None
    season_id: Optional[int] = None
    ordering: Ordering = Ordering.ID
    direction: Direction = Direction.ASC
    field: Field = None
    query: Optional[str] = None
    page: Optional[int] = None
    limit: Optional[int] = 10

    def __str__(self):
        if self.limit < 0 or self.limit > 100:
            raise ValueError("Limit больше 100 или меньше 0")

        return {
            "tv_series_id": self.tv_series_id,
            "season_id": self.season_id,
            "ordering": self.ordering.value,
            "direction": self.direction.value,
            "field": self.field.value,
            "query": self.query,
            "page": self.page,
            "limit": self.limit,
        }
