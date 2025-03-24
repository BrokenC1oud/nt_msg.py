from collections import defaultdict
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


__all__ = ["DatabaseManager"]


class DatabaseManager:
    _models = defaultdict(defaultdict)
    _loaded = set()
    _sessions = {}

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
    
    def group_messages(self):
        return self._sessions["nt_msg"].query(self._models["nt_msg"]["group_msg_table"])


from .models import *
