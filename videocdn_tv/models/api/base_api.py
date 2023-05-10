from datetime import datetime
from typing import Optional

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
    blocked: Optional[bool]
    preview_iframe_src: Optional[str]
    iframe_src: str
    iframe: Optional[str]
    translations: Optional[list[Translation]] = None
