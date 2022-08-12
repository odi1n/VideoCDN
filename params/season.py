from dataclasses import dataclass

from type.direction import Direction
from type.ordering import Ordering


@dataclass
class ParamsSeason:
    tv_series_id: int = None
    ordering: Ordering = Ordering.ID
    direction: Direction = Direction.ASC
    page: int = None
    limit: int = 10

    def __str__(self):
        return {'tv_series_id': self.tv_series_id,
                'ordering': self.ordering.value,
                'direction': self.direction.value,
                'page': self.page,
                'limit': self.limit}
