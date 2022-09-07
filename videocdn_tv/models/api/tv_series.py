from typing import List

from videocdn_tv.models.api.base_api import BaseApi
from videocdn_tv.models.contents import Episode


class TvSeries(BaseApi):
    season_count: int
    episode_count: int
    last_episode_id: int = None
    start_date: str
    end_date: str = None
    episodes: List[Episode]
