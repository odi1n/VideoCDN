from __future__ import annotations

from pydantic import BaseModel


class Translation(BaseModel):
    id: int
    title: str
    priority: int
    iframe_src: str
    iframe: str
    short_title: str
    smart_title: str
    shorter_title: str

    episodes_count: int = None
    source_quality: str = None
    max_quality: int = None