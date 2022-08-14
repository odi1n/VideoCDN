from __future__ import annotations

from typing import List

from pydantic import BaseModel

from videocdn_tv.models.api import Movie, Anime, TvSeries, AnimeTvSeries, ShowTvSeries
from videocdn_tv.models.episodes import ShowTvSeriesEpisode, AnimeTvSeriesEpisode, TvSeriesEpisode
from videocdn_tv.models.seasons import ShowTvSeriesSeason, AnimeTvSeriesSeason, TvSeriesSeason


class ContentBase(BaseModel):
    result: bool
    current_page: int
    first_page_url: str
    from_: int = 0
    last_page: int
    last_page_url: str
    next_page_url: str = None
    path: str
    per_page: int
    prev_page_url: str = None
    to: int = None
    total: int = None
    total_count: int = None


class MovieContent(ContentBase):
    data: List[Movie]


class AnimeContent(ContentBase):
    data: List[Anime]


class TvSeriesContent(ContentBase):
    data: List[TvSeries]


class TvSeriesSeasonsContent(ContentBase):
    data: List[TvSeriesSeason]


class TvSeriesEpisodesContent(ContentBase):
    data: List[TvSeriesEpisode]


class AnimeTvSeriesContent(ContentBase):
    data: List[AnimeTvSeries]


class AnimeTvSeriesSeasonsContent(ContentBase):
    data: List[AnimeTvSeriesSeason]


class AnimeTvSeriesEpisodesContent(ContentBase):
    data: List[AnimeTvSeriesEpisode]


class ShowTvSeriesContent(ContentBase):
    data: List[ShowTvSeries]


class ShowTvSeriesSeasonsContent(ContentBase):
    data: List[ShowTvSeriesSeason]


class ShowTvSeriesEpisodesContent(ContentBase):
    data: List[ShowTvSeriesEpisode]
