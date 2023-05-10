from datetime import datetime
from typing import List, Optional

from videocdn_tv.models.api.base_api import BaseApi
from videocdn_tv.models.contents import Episode


class TvSeries(BaseApi):
    season_count: int
    episode_count: int
    last_episode_id: Optional[int] = None
    start_date: datetime
    end_date: Optional[datetime] = None
    episodes: List[Episode]
