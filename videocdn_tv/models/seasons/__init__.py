from datetime import datetime
from typing import List

from pydantic import BaseModel

from videocdn_tv.models.contents import Episode


class Season(BaseModel):
    id: int
    tv_series_id: int
    num: str
    ru_title: str
    orig_title: str
    episode_count: int
    start_date: datetime
    end_date: datetime
    created: datetime
    episodes: List[Episode]


class TvSeriesSeason(Season):
    pass


class AnimeTvSeriesSeason(Season):
    en_title: str
    other_title: str = None


class ShowTvSeriesSeason(Season):
    pass
