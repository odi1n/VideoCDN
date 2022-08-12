from dataclasses import dataclass

from type.direction import Direction
from type.field import Field
from type.ordering import Ordering


@dataclass
class ParamsContent:
    ordering: Ordering = Ordering.ID
    direction: Direction = Direction.ASC
    field: Field = None
    query: str = None
    translation: int = None
    year: int = None
    page: int = None
    limit: int = 10

    def __str__(self):
        return {'ordering': self.ordering.value,
                'direction': self.direction.value,
                'field': self.field.value if self.field is not None else None,
                'query': self.query,
                'translation': self.translation,
                'year': self.year,
                'page': self.page,
                'limit': self.limit}
