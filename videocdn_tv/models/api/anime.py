from typing import List

from videocdn_tv.models.api.base_api import BaseApi
from videocdn_tv.models.contents import Media


class Anime(BaseApi):
    en_title: str = None
    other_title: str = None
    default_media_id: str = None
    worldart_id: str = None
    released: str
    media: List[Media]
    year: str
    content_type: str
