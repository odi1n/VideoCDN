from dataclasses import dataclass

from type.direction import Direction
from type.field import Field
from type.ordering import Ordering


@dataclass
class ParamsEpisode:
    tv_series_id: int = None
    season_id: int = None
    ordering: Ordering = Ordering.ID
    direction: Direction = Direction.ASC
    field: Field = None
    query: str = None
    page: int = None
    limit: int = 10

    def __str__(self):
        return {'tv_series_id': self.tv_series_id,
                'season_id': self.season_id,
                'ordering': self.ordering.value,
                'direction': self.direction.value,
                'field': self.field.value,
                'query': self.query,
                'page': self.page,
                'limit': self.limit}
