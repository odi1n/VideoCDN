from __future__ import annotations

from typing import List

from pydantic import BaseModel

from videocdn_tv.models.contents import Media


class Episode(BaseModel):
    id: int
    tv_series_id: int
    season_id: int
    num: str
    season_num: int
    ru_title: str
    orig_title: str
    imdb_id: str = None
    kinopoisk_id: str
    released: str
    ru_released: str
    created: str
    media: List[Media]


class TvSeriesEpisode(Episode):
    pass


class AnimeTvSeriesEpisode(Episode):
    en_title: str
    other_title: str = None


class ShowTvSeriesEpisode(Episode):
    pass
