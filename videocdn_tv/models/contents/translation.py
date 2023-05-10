from __future__ import annotations

from typing import Optional

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

    episodes_count: Optional[int] = None
    source_quality: Optional[str] = None
    max_quality: Optional[int] = None
