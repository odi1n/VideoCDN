from pydantic import BaseModel


class Qualitie(BaseModel):
    id: int
    url: str
    resolution: int
    media_id: int
