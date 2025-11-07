import dataclasses
from typing import Optional

from ..value_objects import Name, Photo
from .user import User


@dataclasses.dataclass
class VinylRecord:
    id: str
    band: Name
    album: Name
    year: int
    number_of_tracks: int
    photo: Photo
    user_id: Optional[str] = None
    user: Optional[User] = None
