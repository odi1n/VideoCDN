from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from videocdn_tv.models.api import Anime, AnimeTvSeries, Movie, ShowTvSeries, TvSeries
from videocdn_tv.models.episodes import (
    AnimeTvSeriesEpisode,
    ShowTvSeriesEpisode,
    TvSeriesEpisode,
)
from videocdn_tv.models.seasons import (
    AnimeTvSeriesSeason,
    ShowTvSeriesSeason,
    TvSeriesSeason,
)


class ContentBase(BaseModel):
    result: bool
    current_page: int
    first_page_url: str
    from_: int = 0
    last_page: int
    last_page_url: str
    next_page_url: Optional[str] = None
    path: str
    per_page: int
    prev_page_url: Optional[str] = None
    to: Optional[int] = None
    total: Optional[int] = None
    total_count: Optional[int] = None


class MovieContent(ContentBase):
    data: list[Movie]


class AnimeContent(ContentBase):
    data: list[Anime]


class TvSeriesContent(ContentBase):
    data: list[TvSeries]


class TvSeriesSeasonsContent(ContentBase):
    data: list[TvSeriesSeason]


class TvSeriesEpisodesContent(ContentBase):
    data: list[TvSeriesEpisode]


class AnimeTvSeriesContent(ContentBase):
    data: list[AnimeTvSeries]


class AnimeTvSeriesSeasonsContent(ContentBase):
    data: list[AnimeTvSeriesSeason]


class AnimeTvSeriesEpisodesContent(ContentBase):
    data: list[AnimeTvSeriesEpisode]


class ShowTvSeriesContent(ContentBase):
    data: list[ShowTvSeries]


class ShowTvSeriesSeasonsContent(ContentBase):
    data: list[ShowTvSeriesSeason]


class ShowTvSeriesEpisodesContent(ContentBase):
    data: list[ShowTvSeriesEpisode]
