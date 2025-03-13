from abc import ABC, abstractmethod
import blackboxprotobuf
from pydantic import BaseModel
from typing import List, Type, TypeVar

from collections import defaultdict

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
        except ValueError:
            return UnsupportedElement(data=None)


class Element(ABC, BaseModel):
    ...

    @classmethod
    @abstractmethod
    def decode(cls, data) -> E:
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class UnsupportedElement(Element):
    """ data is None when error raised in parsing, is dict when no parse function found """
    data: dict | None

    @classmethod
    def decode(cls, data):
        return UnsupportedElement(data=data)

    def __str__(self):
        return "不支持的消息"


@ElementRegistry.register(elem_id=1)
class Text(Element):
    content: str | None

    @classmethod
    def decode(cls, data):
        if not isinstance(data.get("45101"), bytes):
            return Text(content=None)
        return Text(content=data["45101"].decode())

    def __str__(self):
        return self.content


@ElementRegistry.register(elem_id=2)
class Image(Element):
    filename: str | None
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
            else:
                alt = None
        else:
            alt = None

        return Image(
            filename=filename if isinstance(filename := (data["45402"]), str) else None,
            width=data["45411"],
            height=data["45412"],
            path=data.get("45812"),
            alt=alt,
        )

    def __str__(self):
        return self.alt if self.alt else ""


@ElementRegistry.register(elem_id=3)
class FileElement(Element):
    hash: str | None
    path: str | None


    @classmethod
    def decode(cls, data):
        return FileElement(
            hash=hash.hex() if isinstance(hash:=data.get("45406"), bytes) else None,
            path=path.decode() if isinstance(path:=data.get("45954"), bytes) else None,
        )

    def __str__(self):
        return "[文件]"
    

@ElementRegistry.register(elem_id=4)
class AudioElement(Element):
    filename: str
    hash: str | None


    @classmethod
    def decode(cls, data):
        return AudioElement(
            filename=data.get("45402"),
            hash=hash.hex() if isinstance(hash:=data.get("45406"), bytes) else None,
        )
    

    def __str__(self):
        return "[语音消息]"


@ElementRegistry.register(elem_id=5)
class VideoElement(Element):
    filename: str | None
    hash: str | None


    @classmethod
    def decode(cls, data):
        return VideoElement(
            filename=data.get("40402"),
            hash=hash.hex() if isinstance(hash:=data.get("45406"), bytes) else None
        )
    

    def __str__(self):
        return "[视频消息]"


@ElementRegistry.register(elem_id=6)
class EmojiElement(Element):
    ID: int

    @classmethod
    def decode(cls, data):
        return EmojiElement(
            ID=data.get("47601")  # -> emoji.db / base_sys_emoji_table / 81211
        )

    def __str__(self):
        return "[Emoji表情]"


@ElementRegistry.register(elem_id=7)
class Reply(Element):
    source_seq: int | None
    source_sender_uin: str | None
    source_sender_qq: int | None
    source_time: int | None
    source_content: 'Message'

    @classmethod
    def decode(cls, data):
        return Reply(
            source_seq=data.get("47402"),
            source_sender_uin=sender_uin if isinstance(sender_uin:=data.get("40020"), str) else None,
            source_sender_qq=data.get("47403"),
            source_time=data.get("47404"),
            source_content=Message.from_reply(data.get("47423"))
        )

    def __str__(self):
        return ""


@ElementRegistry.register(elem_id=8)
class SystemNotificationElement(Element):
    @classmethod
    def decode(cls, data):
        # 47705 -> sender
        # 47716 -> withdrawer
        # 47713 -> suffix
        # 49154 or 45003 -> type I guess (1 -> withdraw)
        return WithdrawNotifyElement.system_decode(data)

    @classmethod
    def system_decode(cls, data):
        raise NotImplementedError

    def __str__(self):
        return "[系统消息]"


class WithdrawNotifyElement(SystemNotificationElement):
    sender: str | None
    withdrawer: str | None
    suffix: str | None

    @classmethod
    def system_decode(cls, data):
        return WithdrawNotifyElement(
            sender=sender if isinstance(sender:=data.get("47705"), str) else None,
            withdrawer=withdrawer if isinstance(withdrawer:=data.get("47716"), str) else None,
            suffix=suffix if (suffix:=data.get("47713")) else None,
        )

    def __str__(self):
        return "撤回了一条消息"


@ElementRegistry.register(elem_id=10)
class AppElement(Element):
    data: str

    @classmethod
    def decode(cls, data):
        return AppElement(
            data=data.get("47901").decode()
        )

    def __str__(self):
        return "[应用消息]"


@ElementRegistry.register(elem_id=11)
class StickerElement(Element):
    alt: str | None
    ID: str | None

    @classmethod
    def decode(cls, data):
        return StickerElement(
            alt=data["80900"].decode() if isinstance(data["80900"], bytes) else None,
            ID=data["80903"].hex() if isinstance(data["80903"], bytes) else None,
        )

    def __str__(self):
        return self.alt if self.alt else ""


@ElementRegistry.register(elem_id=14)
class BotCardElement(Element):
    # TODO: i guess
    @classmethod
    def decode(cls, data):
        return BotCardElement()

    def __str__(self):
        return "[Bot卡片]"


@ElementRegistry.register(elem_id=16)
class XMLElement(Element):
    @classmethod
    def decode(cls, data):
        # TODO: Example Missing
        return ForwardedMessagesXMLElement.xml_decode(data=data["48602"])

    @classmethod
    def xml_decode(cls, data):
        raise NotImplementedError

    def __str__(self):
        return ""


class ForwardedMessagesXMLElement(XMLElement):
    @classmethod
    def xml_decode(cls, data):
        # TODO
        return ForwardedMessagesXMLElement()

    def __str__(self):
        return "[聊天记录]"


@ElementRegistry.register(elem_id=17)
class BotCardMobileElement(Element):
    # TODO: i guess
    @classmethod
    def decode(cls, data):
        return BotCardMobileElement()

    def __str__(self):
        return "[Bot卡片]"


class Message(BaseModel):
    ID: int | None
    seq: int | None
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

    @classmethod
    def from_reply(cls, embed) -> 'Message':
        if embed is None:
            embed = []
        if isinstance(embed, dict):
            embed = [embed]

        elements = [ElementRegistry.decode(_) for _ in embed]
        return Message(ID=None, seq=None, elements=elements)
