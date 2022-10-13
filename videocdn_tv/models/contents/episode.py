from datetime import datetime
from typing import List

from pydantic import BaseModel

from videocdn_tv.models.contents.media import Media


class Episode(BaseModel):
    id: int
    tv_series_id: int
    season_id: int
    num: str
    season_num: int = None
    ru_title: str
    orig_title: str
    imdb_id: str = None
    kinopoisk_id: str = None
    released: datetime
    ru_released: datetime = None
    created: datetime
    media: List[Media]
