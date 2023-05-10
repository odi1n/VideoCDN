from __future__ import annotations

from pydantic import BaseModel

from videocdn_tv.models.api import Anime, AnimeTvSeries, Movie, ShowTvSeries, TvSeries, Translations
from videocdn_tv.models.base import ContentBase
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


class TranslationModel(BaseModel):
    result: bool
    data: list[Translations]


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
