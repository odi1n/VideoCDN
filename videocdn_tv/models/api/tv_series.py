from typing import List

from pydantic import BaseModel

from videocdn_tv.models.contents import Translation, Episode


class TvSeries(BaseModel):
    id: int
    ru_title: str
    orig_title: str
    imdb_id: str
    kinopoisk_id: str
    season_count: int
    episode_count: int
    last_episode_id: int
    start_date: str
    end_date: str = None
    created: str
    updated: str
    blocked: int
    preview_iframe_src: str
    iframe_src: str
    iframe: str
    translations: List[Translation]
    episodes: List[Episode]
