from datetime import datetime
from typing import Optional

from videocdn_tv.models.api.base_api import BaseApi
from videocdn_tv.models.contents import Episode


class TvSeries(BaseApi):
    season_count: Optional[int]
    episode_count: Optional[int]
    last_episode_id: Optional[int]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    episodes: list[Episode]
