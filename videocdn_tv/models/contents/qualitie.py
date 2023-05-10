from typing import Optional

from pydantic import BaseModel


class Qualitie(BaseModel):
    id: Optional[int]
    url: str
    resolution: int
    media_id: int
