from collections import defaultdict
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm.query import Query


__all__ = ["DatabaseManager"]


class DatabaseManager:
    _models = defaultdict(defaultdict)
    _loaded: set[str] = set()
    _sessions: dict[str, Session] = {}

    @classmethod
    def register_model(cls, db_id: str) -> callable:
        def wrapper(model):
            cls._models[db_id][model.__tablename__] = model
            return model
        return wrapper
    
    def __new__(cls):
        # Check for existing files corresponding to registered models and add them to the `_load` set
        for db_filename in cls._models.keys():
            if os.path.exists(f"{db_filename}.decrypt.db"):
                cls._loaded.add(db_filename)
        for _ in cls._loaded:
            cls._sessions[_] = Session(create_engine(f"sqlite:///./{_}.decrypt.db"))
        return super(DatabaseManager, cls).__new__(cls)
    
    def __init__(self):
        pass

    def private_messages(self) -> Query:
        return self._sessions["nt_msg"].query(self._models["nt_msg"]["c2c_msg_table"])
    
    def group_messages(self) -> Query:
        return self._sessions["nt_msg"].query(self._models["nt_msg"]["group_msg_table"])
    
    def buddy_info(self) -> Query:
        return self._sessions["profile_info"].query(self._models["profile_info"]["profile_info_v6"])
    
    def get_buddy(self, *, uid: str, uin: int):
        ...


from .models import *
