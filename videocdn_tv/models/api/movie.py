from datetime import datetime
from typing import Optional

from videocdn_tv.models.api.base_api import BaseApi
from videocdn_tv.models.contents import Media


class Movie(BaseApi):
    default_media_id: Optional[str] = None
    released: Optional[datetime] = None
    media: list[Media]
    year: str
    content_type: str
