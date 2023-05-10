from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from videocdn_tv.models.contents.media import Media


class Episode(BaseModel):
    id: Optional[int]
    tv_series_id: int
    season_id: int
    num: str
    season_num: Optional[int]
    ru_title: str
    orig_title: str
    imdb_id: Optional[str]
    kinopoisk_id: Optional[str]
    released: datetime
    ru_released: Optional[datetime]
    created: datetime
    media: list[Media]
