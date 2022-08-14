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


class Datum(BaseModel):
    id: int
    ru_title: str
    orig_title: str
    imdb_id: str = None
    kinopoisk_id: int
    season_count: int = None
    episode_count: int = None
    last_episode_id: int = None
    default_media_id: Any
    start_date: str = None
    end_date: str = None
    created: str
    released: str
    updated: str
    blocked: int
    preview_iframe_src: str
    iframe_src: str
    iframe: str
    year: str
    content_type: str
    translations: List[Translations]


class ContentModel(BaseModel):
    result: bool
    data: List[Datum]
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
