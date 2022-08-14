from __future__ import annotations

from typing import Any, List

from pydantic import BaseModel


class Translations(BaseModel):
    id: int
    title: str
    priority: int
    iframe_src: str
    iframe: str
    short_title: str
    smart_title: str
    shorter_title: str


class Qualities(BaseModel):
    id: int
    url: str
    resolution: int
    media_id: int


class Media(BaseModel):
    id: int
    translation_id: int
    content_id: int
    content_type: str
    tv_series_id: str = None
    source_quality: str
    max_quality: int
    path: str
    duration: int
    created: str
    accepted: str
    deleted_at: str = None
    blocked: int
    count_download: int
    qualities: List[Qualities]


class Movies(BaseModel):
    id: int
    ru_title: str
    orig_title: str
    imdb_id: str = None
    kinopoisk_id: int
    default_media_id: Any
    created: str
    released: str
    updated: str
    blocked: int
    media: List[Media]


class Content(BaseModel):
    result: bool
    data_movies: List[Movies]
    current_page: int
    first_page_url: str
    from_: int = 0
    last_page: int
    last_page_url: str
    next_page_url: str
    path: str
    per_page: int
    prev_page_url: str = None
    to: int
    total: int
    total_count: int
