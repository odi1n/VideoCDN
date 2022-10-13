from datetime import datetime
from typing import List

from videocdn_tv.models.api.base_api import BaseApi
from videocdn_tv.models.contents import Media


class Movie(BaseApi):
    default_media_id: str = None
    released: datetime
    media: List[Media]
    year: str
    content_type: str
