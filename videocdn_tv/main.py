from videocdn_tv.link import *
from videocdn_tv.models.content import (
    MovieContent,
    AnimeContent,
    TvSeriesContent,
    AnimeTvSeriesContent,
    ShowTvSeriesContent
)
from videocdn_tv.models.translation import TranslationModel

from videocdn_tv.params import *
from videocdn_tv.request import get_request


class VideoCDN:
    def __init__(self, api_token: str):
        self.params = {'api_token': api_token}

    def get_translations(self) -> TranslationModel:
        return TranslationModel(**get_request(self, TRANSLATIONS))

    def get_movies(self, params: ParamsContent) -> MovieContent:
        return MovieContent(**get_request(self, MOVIES, params))

    def get_animes(self, params: ParamsContent) -> AnimeContent:
        return AnimeContent(**get_request(self, MOVIES, params))

    def get_tv_series(self, params: ParamsContent) -> TvSeriesContent:
        return TvSeriesContent(**get_request(self, TV_SERIES, params))

    def get_tv_series_seasons(self, params: ParamsSeason) -> Content:
        return Content(**get_request(self, TV_SERIES_SEASONS, params))

    def get_tv_series_episodes(self, params: ParamsEpisode) -> Content:
        return Content(**get_request(self, TV_SERIES_EPISODES, params))

    def get_anime_tv_series(self, params: ParamsContent) -> AnimeTvSeriesContent:
        return AnimeTvSeriesContent(**get_request(self, ANIME_TV_SERIES, params))

    def get_anime_tv_series_seasons(self, params: ParamsSeason) -> Content:
        return Content(**get_request(self, ANIME_TV_SERIES_SEASONS, params))

    def get_anime_tv_series_episodes(self, params: ParamsEpisode) -> Content:
        return Content(**get_request(self, ANIME_TV_SERIES_EPISODES, params))

    def get_show_tv_series(self, params: ParamsContent) -> ShowTvSeriesContent:
        return ShowTvSeriesContent(**get_request(self, SHOW_TV_SERIES, params))

    def get_show_tv_series_season(self, params: ParamsSeason) -> Content:
        return Content(**get_request(self, SHOW_TV_SERIES_SEASONS, params))

    def get_show_tv_series_episodes(self, params: ParamsEpisode) -> Content:
        return Content(**get_request(self, SHOW_TV_SERIES_EPISODES, params))
