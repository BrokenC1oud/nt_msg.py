from abc import ABC
import dataclasses

from .asset import Image


@dataclasses.dataclass
class Contact(ABC):
    uid: str
    uin: int
    name: str
    avatar: Image


class Buddy(Contact):
    ...


class Group(Contact):
    ...
