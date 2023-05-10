from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from videocdn_tv.models.contents.qualitie import Qualitie


class Media(BaseModel):
    id: int
    translation_id: int
    content_id: int
    content_type: str
    tv_series_id: Optional[str]
    source_quality: str
    max_quality: int
    path: str
    duration: int
    created: Optional[datetime]
    accepted: Optional[str]
    deleted_at: Optional[str]
    blocked: Optional[bool]
    count_download: Optional[int]
    qualities: Optional[list[Qualitie]]
