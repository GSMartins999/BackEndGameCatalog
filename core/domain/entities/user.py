import dataclasses

from ..value_objects import Email, Password


@dataclasses.dataclass
class User:
    id: str
    email: Email
    password: Password