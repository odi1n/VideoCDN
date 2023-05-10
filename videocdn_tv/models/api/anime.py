from datetime import datetime
from typing import List, Optional

from videocdn_tv.models.api.base_api import BaseApi
from videocdn_tv.models.contents import Media


class Anime(BaseApi):
    en_title: Optional[str] = None
    other_title: Optional[str] = None
    default_media_id: Optional[str] = None
    worldart_id: Optional[str] = None
    released: datetime
    media: List[Media]
    year: str
    content_type: str
