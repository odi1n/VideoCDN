from pydantic import BaseModel


class Translations(BaseModel):
    id: int
    title: str
    priority: int
    short_title: str
    smart_title: str
    shorter_title: str