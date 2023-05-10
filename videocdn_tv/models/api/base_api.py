from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from videocdn_tv.models.contents import Translation


class BaseApi(BaseModel):
    id: int
    ru_title: str
    orig_title: str
    imdb_id: Optional[str] = None
    kinopoisk_id: Optional[int] = None
    created: datetime
    updated: Optional[datetime] = None
    blocked: int
    preview_iframe_src: str
    iframe_src: str
    iframe: str
    translations: Optional[List[Translation]] = None
