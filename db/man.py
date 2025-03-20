from collections import defaultdict


__all__ = ["DatabaseManager"]


class DatabaseManager:
    _models = defaultdict(list)

    @classmethod
    def register_model(cls, db_id: str) -> callable:
        def wrapper(model):
            cls._models[db_id].append(model)
            return model

        return wrapper

    def __init__(self):
        pass


from .models import *
