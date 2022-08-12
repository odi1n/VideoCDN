from dataclasses import dataclass

from videocdn_tv.type.direction import Direction
from videocdn_tv.type.field import Field
from videocdn_tv.type.ordering import Ordering


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
        if self.limit < 0 or self.limit > 100:
            raise ValueError("Limit больше 100 или меньше 0")

        return {'ordering': self.ordering.value,
                'direction': self.direction.value,
                'field': self.field.value if self.field is not None else None,
                'query': self.query,
                'translation': self.translation,
                'year': self.year,
                'page': self.page,
                'limit': self.limit}
