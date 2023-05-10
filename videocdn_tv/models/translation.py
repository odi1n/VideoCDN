from __future__ import annotations

from pydantic import BaseModel


class Datum(BaseModel):
    id: int
    title: str
    priority: int
    short_title: str
    smart_title: str
    shorter_title: str


class TranslationModel(BaseModel):
    result: bool
    data: list[Datum]
