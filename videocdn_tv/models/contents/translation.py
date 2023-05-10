from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Translation(BaseModel):
    id: int
    title: Optional[str]
    priority: Optional[int]
    iframe_src: str
    iframe: Optional[str]
    short_title: Optional[str]
    smart_title: Optional[str]
    shorter_title: Optional[str]

    episodes_count: Optional[int]
    source_quality: Optional[str]
    max_quality: Optional[int]
