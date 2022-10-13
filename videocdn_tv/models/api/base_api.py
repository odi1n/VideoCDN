from datetime import datetime
from typing import List

from pydantic import BaseModel

from videocdn_tv.models.contents import Translation


class BaseApi(BaseModel):
    id: int
    ru_title: str
    orig_title: str
    imdb_id: str = None
    kinopoisk_id: int = None
    created: datetime
    updated: datetime = None
    blocked: int
    preview_iframe_src: str
    iframe_src: str
    iframe: str
    translations: List[Translation] = None
