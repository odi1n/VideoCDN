import enum


class Ordering(str, enum.Enum):
    ID = "id"
    CREATED = "created"
    RELEASED = "released"
