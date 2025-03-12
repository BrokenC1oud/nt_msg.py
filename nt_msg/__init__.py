from abc import ABC, abstractmethod
import blackboxprotobuf
from pydantic import BaseModel
from typing import List, Type, TypeVar
import lxml.etree
from io import BytesIO

from collections import defaultdict
from pprint import pprint

from db import GroupMessage

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
    @abstractmethod
    def decode(cls, data) -> E:
        raise NotImplementedError


class UnsupportedElement(Element):
    """ data is None when error raised in parsing, is dict when no parse function found """
    data: dict | None


    @classmethod
    def decode(cls, data):
        return UnsupportedElement(data=data)
    

@ElementRegistry.register(elem_id=1)
class Text(Element):
    content: str


    @classmethod
    def decode(cls, data):
        if not isinstance(data.get("45101"), bytes):
            return UnsupportedElement(data=None)
        return Text(content=data["45101"].decode())
    

@ElementRegistry.register(elem_id=2)
class Image(Element):
    filename: str
    width: int
    height: int
    path: str | None
    alt: str | None

    
    @classmethod
    def decode(cls, data):
        alt = data.get("45815")
        if isinstance(alt, list):
            if isinstance(alt[0], bytes):
                alt = alt[0].decode()
            else: alt = None
        else: alt = None

        return Image(
            filename=data["45402"],
            width=data["45411"],
            height=data["45412"],
            path=data.get("45812"),
            alt=alt,
        )


@ElementRegistry.register(elem_id=7)
class Reply(Element):
    @classmethod
    def decode(cls, data):
        return Reply()
    

@ElementRegistry.register(elem_id=16)
class XMLElement(Element):
    @classmethod
    def decode(cls, data):
        # TODO: Example Missing
        return ForwardedMessagesXMLElement.xml_decode(data=data["48602"])
    

    @classmethod
    def xml_decode(cls, data):
        raise NotImplementedError


class ForwardedMessagesXMLElement(XMLElement):
    @classmethod
    def xml_decode(cls, data):
        # TODO
        return ForwardedMessagesXMLElement()
    

@ElementRegistry.register(elem_id=11)
class StickerElement(Element):
    alt: str


    @classmethod
    def decode(cls, data):
        return StickerElement(unk=data["80900"].decode())


class Message(BaseModel):
    ID: int
    seq: int
    elements: List['Element']


    @classmethod
    def from_db(cls, dbo: GroupMessage) -> 'Message':
        if dbo.message_body is None:
            elements = []
        else:
            raw_elements, _ = blackboxprotobuf.decode_message(dbo.message_body)
            raw_elements = raw_elements["40800"]
            if isinstance(raw_elements, dict):
                raw_elements = [raw_elements]
            elements = [ElementRegistry.decode(_) for _ in raw_elements]

        return Message(
            ID=dbo.ID,
            seq=dbo.seq,
            elements=elements,
        )
