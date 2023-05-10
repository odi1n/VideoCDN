from dataclasses import dataclass
from typing import Optional

from videocdn_tv.type.direction import Direction
from videocdn_tv.type.ordering import Ordering


@dataclass
class ParamsSeason:
    tv_series_id: Optional[int] = None
    ordering: Ordering = Ordering.ID
    direction: Direction = Direction.ASC
    page: Optional[int] = None
    limit: int = 10

    def __str__(self):
        if self.limit < 0 or self.limit > 100:
            raise ValueError("Limit больше 100 или меньше 0")

        return {
            "tv_series_id": self.tv_series_id,
            "ordering": self.ordering.value,
            "direction": self.direction.value,
            "page": self.page,
            "limit": self.limit,
        }
