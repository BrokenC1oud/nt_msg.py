from abc import ABC
from pydantic import BaseModel
from typing import Type, TypeVar

from collections import defaultdict

E = TypeVar('E', bound="Element")


class ElementRegistry:
    _decoders = defaultdict(lambda: UnsupportedElement)

    @classmethod
    def register(cls, elem_id: int) -> callable:
        def decorator(element_class: Type[E]) -> Type[E]:
            cls._decoders[elem_id] = element_class
            return element_class

        return decorator

    @classmethod
    def decode(cls, data) -> E:
        try:
            return cls._decoders[data.get("45002")].decode(data)
        except ValueError as e:
            return UnsupportedElement()


class Element(ABC, BaseModel):
    ...

    @classmethod
    def decode(cls, data) -> E:
        ...


class UnsupportedElement(Element):
    ...
