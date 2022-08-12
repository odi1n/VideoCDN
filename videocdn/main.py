import json
from typing import Tuple

import requests
from requests import Response

from link import *
from models.content import ContentModel
from models.translation import TranslationModel

from params import *
from request import get_request


class VideoCDN:
    def __init__(self, api_token: str):
        self.params = {'api_token': api_token}

    def get_translations(self) -> Tuple[Response, TranslationModel]:
        response = requests.get(TRANSLATIONS, params=self.params)
        return response, TranslationModel(**json.loads(response.text))

    def get_movies(self, params: ParamsContent) -> Tuple[Response, ContentModel]:
        return get_request(self, MOVIES, params)

    def get_animes(self, params: ParamsContent) -> Tuple[Response, ContentModel]:
        return get_request(self, MOVIES, params)

    def get_tv_series(self, params: ParamsContent) -> Tuple[Response, ContentModel]:
        return get_request(self, TV_SERIES, params)

    def get_tv_series_seasons(self, params: ParamsSeason) -> Tuple[Response, ContentModel]:
        return get_request(self, TV_SERIES_SEASONS, params)

    def get_tv_series_episodes(self, params: ParamsEpisode) -> Tuple[Response, ContentModel]:
        return get_request(self, TV_SERIES_EPISODES, params)

    def get_anime_tv_series(self, params: ParamsContent) -> Tuple[Response, ContentModel]:
        return get_request(self, ANIME_TV_SERIES, params)

    def get_anime_tv_series_seasons(self, params: ParamsSeason) -> Tuple[Response, ContentModel]:
        return get_request(self, ANIME_TV_SERIES_SEASONS, params)

    def get_anime_tv_series_episodes(self, params: ParamsEpisode) -> Tuple[Response, ContentModel]:
        return get_request(self, ANIME_TV_SERIES_EPISODES, params)

    def get_show_tv_series(self, params: ParamsContent) -> Tuple[Response, ContentModel]:
        return get_request(self, SHOW_TV_SERIES, params)

    def get_show_tv_series_season(self, params: ParamsSeason) -> Tuple[Response, ContentModel]:
        return get_request(self, SHOW_TV_SERIES_SEASONS, params)

    def get_show_tv_series_episodes(self, params: ParamsEpisode) -> Tuple[Response, ContentModel]:
        return get_request(self, SHOW_TV_SERIES_EPISODES, params)
