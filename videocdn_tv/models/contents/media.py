from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from videocdn_tv.models.contents.qualitie import Qualitie


class Media(BaseModel):
    id: int
    translation_id: int
    content_id: int
    content_type: str
    tv_series_id: Optional[str] = None
    source_quality: str
    max_quality: int
    path: str
    duration: int
    created: datetime
    accepted: Optional[str] = None
    deleted_at: Optional[str] = None
    blocked: int
    count_download: int
    qualities: Optional[list[Qualitie]] = None
