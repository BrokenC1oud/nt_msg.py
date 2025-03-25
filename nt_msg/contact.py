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
    
    @abstractmethod
    def messages(self, dbman: DatabaseManager) -> Query:
        raise NotImplementedError


class Buddy(Contact):
    def messages(self, dbman: DatabaseManager) -> Query:
        return dbman.private_messages().filter_by(contact_qq=self.uin)


class Group(Contact):
    ...
