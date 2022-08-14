from typing import List

from pydantic import BaseModel

from videocdn_tv.models.contents import Translation, Episode


class AnimeTvSeries(BaseModel):
    id: int
    ru_title: str
    orig_title: str
    en_title: str
    other_title: str
    imdb_id: str
    kinopoisk_id: str
    worldart_id: str
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