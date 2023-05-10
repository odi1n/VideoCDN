from datetime import datetime
from typing import Optional

from videocdn_tv.models.api.base_api import BaseApi
from videocdn_tv.models.contents import Media


class Anime(BaseApi):
    en_title: Optional[str]
    other_title: Optional[str]
    default_media_id: Optional[str]
    worldart_id: Optional[str]
    released: Optional[datetime]
    media: list[Media]
    year: str
    content_type: str
