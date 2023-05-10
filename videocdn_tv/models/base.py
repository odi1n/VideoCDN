from typing import Optional

from pydantic import BaseModel


class ContentBase(BaseModel):
    result: bool
    current_page: int
    first_page_url: str
    from_: int = 0
    last_page: int
    last_page_url: str
    next_page_url: Optional[str] = None
    path: str
    per_page: int
    prev_page_url: Optional[str] = None
    to: Optional[int] = None
    total: Optional[int] = None
    total_count: Optional[int] = None
