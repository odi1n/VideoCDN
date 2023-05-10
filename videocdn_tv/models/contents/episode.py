from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from videocdn_tv.models.contents.media import Media


class Episode(BaseModel):
    id: int
    tv_series_id: int
    season_id: int
    num: str
    season_num: Optional[int] = None
    ru_title: str
    orig_title: str
    imdb_id: Optional[str] = None
    kinopoisk_id: Optional[str] = None
    released: datetime
    ru_released: Optional[datetime] = None
    created: datetime
    media: List[Media]
