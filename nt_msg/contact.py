from abc import ABC, abstractmethod
import dataclasses

from typing import Self

from sqlalchemy.orm.query import Query

from .asset import Image
from db import DatabaseManager, models


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
