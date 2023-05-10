from typing import Optional

from videocdn_tv.type.direction import Direction
from videocdn_tv.type.ordering import Ordering


class BaseParams:
    ordering: Ordering = Ordering.ID
    direction: Direction = Direction.ASC
    page: Optional[int] = None
    limit: int = 10

    def validate(self) -> None:
        if self.limit < 0 or self.limit > 100:
            raise ValueError("Limit больше 100 или меньше 0")

    def as_dict(self) -> dict:
        return {
            "ordering": self.ordering.value,
            "direction": self.direction.value,
            "page": self.page,
            "limit": self.limit,
        }
