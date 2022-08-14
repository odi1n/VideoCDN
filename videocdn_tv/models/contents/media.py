from typing import List

from pydantic import BaseModel

from videocdn_tv.models.contents.qualities import Qualitie


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
    qualities: List[Qualitie]
