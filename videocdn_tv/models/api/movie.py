from typing import List

from pydantic import BaseModel

from videocdn_tv.models.contents import Media, Translation


class Movie(BaseModel):
    id: int
    ru_title: str
    orig_title: str
    imdb_id: str = None
    kinopoisk_id: int = None
    default_media_id: str = None
    created: str
    released: str
    updated: str = None
    blocked: int
    media: List[Media]
    preview_iframe_src: str
    iframe_src: str
    iframe: str
    translations: List[Translation] = None
    year: str
    content_type: str
