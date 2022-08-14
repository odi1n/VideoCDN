from __future__ import annotations

from typing import List

from pydantic import BaseModel

from videocdn_tv.models.api import Movie, Anime, TvSeries, AnimeTvSeries, ShowTvSeries
from videocdn_tv.models.seasons import ShowTvSeriesSeason, AnimeTVSeriesSeason, TvSeriesSeason


class ContentBase(BaseModel):
    result: bool
    current_page: int
    first_page_url: str
    from_: int = 0
    last_page: int
    last_page_url: str
    next_page_url: str
    path: str
    per_page: int
    prev_page_url: str = None
    to: int
    total: int
    total_count: int


class MovieContent(ContentBase):
    data: List[Movie]


class AnimeContent(ContentBase):
    data: List[Anime]


class TvSeriesContent(ContentBase):
    data: List[TvSeries]


class TvSeriesSeasonsContent(ContentBase):
    data: List[TvSeriesSeason]


class AnimeTvSeriesContent(ContentBase):
    data: List[AnimeTvSeries]


class AnimeTvSeriesSeasonsContent(ContentBase):
    data: List[AnimeTVSeriesSeason]


class ShowTvSeriesContent(ContentBase):
    data: List[ShowTvSeries]


class ShowTvSeriesSeasonsContent(ContentBase):
    data: List[ShowTvSeriesSeason]
