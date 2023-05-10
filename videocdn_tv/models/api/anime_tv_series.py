from datetime import datetime
from typing import Optional

from videocdn_tv.models.api.base_api import BaseApi
from videocdn_tv.models.contents import Episode


class AnimeTvSeries(BaseApi):
    en_title: str
    other_title: Optional[str] = None
    worldart_id: Optional[str] = None
    season_count: int
    episode_count: int
    last_episode_id: int
    start_date: datetime
    end_date: Optional[datetime] = None
    episodes: list[Episode]
