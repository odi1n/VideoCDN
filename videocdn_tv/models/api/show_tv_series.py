from typing import List

from videocdn_tv.models.api.base_api import BaseApi
from videocdn_tv.models.contents import Episode


class ShowTvSeries(BaseApi):
    season_count: int
    episode_count: int
    last_episode_id: int
    start_date: str
    end_date: str = None
    episodes: List[Episode]
