from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, LargeBinary, Text

from .man import DatabaseManager


__all__ = [
    "PrivateMessage",
    "GroupMessage",
    "NTUIDMapping",
    "StickerMapping",
]


class Model(DeclarativeBase):
    ...


@DatabaseManager.register_model("nt_msg")
class PrivateMessage(Model):
    """
    Private Message Table
    nt_msg.db -> c2c_msg_table
    """
    __tablename__ = "c2c_msg_table"
    ID: Mapped[int] = mapped_column("40001", primary_key=True)
    UNK_01: Mapped[int] = mapped_column("40002")
    seq: Mapped[int] = mapped_column("40003")
    UNK_03: Mapped[int] = mapped_column("40010")
    UNK_04: Mapped[int] = mapped_column("40011")
    UNK_05: Mapped[int] = mapped_column("40012")
    UNK_06: Mapped[int] = mapped_column("40013")
    UNK_07: Mapped[str] = mapped_column("40020", String(24))  # Tencent internal UID
    UNK_08: Mapped[int] = mapped_column("40026")
    contact_uid: Mapped[str] = mapped_column("40021", String(24))  # Tencent internal UID
    UNK_10: Mapped[int] = mapped_column("40027")
    UNK_11: Mapped[int] = mapped_column("40040")
    UNK_12: Mapped[int] = mapped_column("40041")
    timestamp: Mapped[int] = mapped_column("40050")  # time message sent
    UNK_14: Mapped[int] = mapped_column("40052")
    UNK_15: Mapped[str] = mapped_column("40090", Text)  # empty
    nick_name: Mapped[str] = mapped_column("40093", Text)  # only self, otherwise basically empty
    message_body: Mapped[bytes] = mapped_column("40800", LargeBinary)  # protobuf
    # protobuf, the message replied to
    reply_body: Mapped[bytes] = mapped_column("40900", LargeBinary)
    UNK_19: Mapped[int] = mapped_column("40105")
    UNK_20: Mapped[int] = mapped_column("40005")
    # time of the day the message was sent, in sec
    timestamp_day: Mapped[int] = mapped_column("40058")
    UNK_22: Mapped[int] = mapped_column("40006")
    UNK_23: Mapped[int] = mapped_column("40100")
    # protobuf, seem to be related to reply, idk
    UNK_24: Mapped[bytes] = mapped_column("40600", LargeBinary)
    UNK_25: Mapped[int] = mapped_column("40060")
    UNK_26: Mapped[int] = mapped_column("40850")
    UNK_27: Mapped[int] = mapped_column("40851")
    UNK_28: Mapped[bytes] = mapped_column("40601", LargeBinary)  # always null
    UNK_29: Mapped[bytes] = mapped_column("40801", LargeBinary)  # protobuf
    # protobuf, insufficient resource, related with file?
    UNK_30: Mapped[bytes] = mapped_column("40605", LargeBinary)
    contact_qq: Mapped[int] = mapped_column("40030")  # qq num
    sender_qq: Mapped[int] = mapped_column("40033")  # qq num
    UNK_33: Mapped[int] = mapped_column("40062")
    UNK_34: Mapped[int] = mapped_column("40083")
    UNK_35: Mapped[int] = mapped_column("40084")


@DatabaseManager.register_model("nt_msg")
class GroupMessage(Model):
    """
    Group Message Table
    nt_msg.db -> group_msg_table
    """
    __tablename__ = "group_msg_table"
    msgId: Mapped[int] = mapped_column("40001", primary_key=True)
    msgRandom: Mapped[int] = mapped_column("40002")
    msgSeq: Mapped[int] = mapped_column("40003")
    chatType: Mapped[int] = mapped_column("40010")  # TODO: Enum
    msgType: Mapped[int] = mapped_column("40011")
    subMsgType: Mapped[int] = mapped_column("40012")
    sendType: Mapped[int] = mapped_column("40013")
    senderUid: Mapped[str] = mapped_column("40020", String(24))
    UNK_08: Mapped[int] = mapped_column("40026")
    peerUid: Mapped[str] = mapped_column("40021", String(24))
    peerUin: Mapped[int] = mapped_column("40027")
    UNK_11: Mapped[int] = mapped_column("40040")
    sendStatus: Mapped[int] = mapped_column("40041")
    msgTime: Mapped[int] = mapped_column("40050")  # UTC+8
    UNK_14: Mapped[int] = mapped_column("40052")
    sendMemberName: Mapped[str] = mapped_column("40090", Text)
    sendNickName: Mapped[str] = mapped_column("40093", Text)
    msgBody: Mapped[bytes] = mapped_column("40800", LargeBinary)  # protobuf
    refBody: Mapped[bytes] = mapped_column("40900", LargeBinary)
    UNK_19: Mapped[int] = mapped_column("40105")
    UNK_20: Mapped[int] = mapped_column("40005")
    msgTimeDay: Mapped[int] = mapped_column("40058")  # UTC+8
    elemId: Mapped[int] = mapped_column("40006")
    atFlag: Mapped[int] = mapped_column("40100")
    msgStatus: Mapped[bytes] = mapped_column("40600", LargeBinary)
    groupState: Mapped[int] = mapped_column("40060")
    refSeq: Mapped[int] = mapped_column("40850")
    UNK_27: Mapped[int] = mapped_column("40851")
    UNK_28: Mapped[bytes] = mapped_column("40601", LargeBinary)  # always null
    UNK_29: Mapped[bytes] = mapped_column("40801", LargeBinary)  # protobuf
    # protobuf, insufficient resource, related with file?
    UNK_30: Mapped[bytes] = mapped_column("40605", LargeBinary)
    groupUin: Mapped[int] = mapped_column("40030")  # qq num
    senderUin: Mapped[int] = mapped_column("40033")  # qq num
    UNK_33: Mapped[int] = mapped_column("40062")
    UNK_34: Mapped[int] = mapped_column("40083")
    UNK_35: Mapped[int] = mapped_column("40084")


@DatabaseManager.register_model("nt_msg")
class NTUIDMapping(Model):
    """
    qqnt uid mapping table
    nt_msg.db -> nt_uid_mapping_table
    """
    __tablename__ = "nt_uid_mapping_table"
    ID: Mapped[int] = mapped_column("48901", primary_key=True)
    uid: Mapped[str] = mapped_column("48902", String(24))
    UNK: Mapped[str] = mapped_column("48912", nullable=True)  # always null
    qq: Mapped[int] = mapped_column("1002")


@DatabaseManager.register_model("emoji")
class SystemEmoji(Model):
    """
    QQ 默认表情数据
    emoji.db -> base_sys_emoji_table
    """
    __tablename__ = "base_sys_emoji_table"
    ID: Mapped[str] = mapped_column("81211", primary_key=True)
    desc: Mapped[str] = mapped_column("81212")
    UNK_01: Mapped[str] = mapped_column("81213")
    UNK_02: Mapped[int] = mapped_column("81214")
    UNK_03: Mapped[int] = mapped_column("81215")
    UNK_04: Mapped[int] = mapped_column("81216")
    UNK_05: Mapped[int] = mapped_column("81217")
    download_link: Mapped[bytes] = mapped_column("81218")
    UNK_06: Mapped[str] = mapped_column("81219")
    UNK_07: Mapped[bytes] = mapped_column("81220")
    special: Mapped[int] = mapped_column("81221")
    UNK_08: Mapped[int] = mapped_column("81222")
    UNK_09: Mapped[int] = mapped_column("81223")
    UNK_10: Mapped[int] = mapped_column("81224")
    UNK_11: Mapped[int] = mapped_column("81225")
    emoji_type: Mapped[int] = mapped_column("81226")
    type_desc: Mapped[str] = mapped_column("81266")
    static_download_link: Mapped[str] = mapped_column("81229")
    apng_link: Mapped[str] = mapped_column("81230")


@DatabaseManager.register_model("emoji")
class BottomeEmoji(Model):
    """
    收藏的原创表情
    emoji.db -> bottom_emoji_table
    """
    __tablename__ = "bottom_emoji_table"
    ID: Mapped[int] = mapped_column("80830", primary_key=True)
    data: Mapped[bytes] = mapped_column("81322")


@DatabaseManager.register_model("emoji")
class EmojiConfig(Model):
    """
    QQ 表情配置
    emoji.db -> emoji_config_storage_table
    """
    __tablename__ = "emoji_config_storage_table"
    ID: Mapped[int] = mapped_column("80401", primary_key=True)
    UNK: Mapped[int] = mapped_column("80402")
    data: Mapped[str] = mapped_column("80403")


@DatabaseManager.register_model("emoji")
class EmojiGroup(Model):
    """
    QQ 表情分组
    emoji.db -> emoji_group_table
    """
    __tablename__ = "emoji_group_table"
    data: Mapped[bytes] = mapped_column("81387", primary_key=True)


@DatabaseManager.register_model("emoji")
class EmojiMiscData(Model):
    """
    QQ 表情杂项数据
    emoji.db -> emoji_misc_data_table
    """
    __tablename__ = "emoji_misc_data_table"
    ID: Mapped[str] = mapped_column("81388", primary_key=True)
    data: Mapped[bytes] = mapped_column("81398")


@DatabaseManager.register_model("emoji")
class FavEmojiInfo(Model):
    """
    QQ 收藏表情信息
    emoji.db -> fav_emoji_info_storage_table
    """
    __tablename__ = "fav_emoji_info_storage_table"
    filename: Mapped[str] = mapped_column("80002", primary_key=True)
    order: Mapped[int] = mapped_column("80001")
    uin: Mapped[str] = mapped_column("1002")
    local_path: Mapped[str] = mapped_column("80012")
    download_url: Mapped[str] = mapped_column("80010")
    md5: Mapped[str] = mapped_column("80011")
    UNK_01: Mapped[str] = mapped_column("80013")
    UNK_02: Mapped[str] = mapped_column("80014")
    UNK_03: Mapped[str] = mapped_column("80211")
    UNK_04: Mapped[int] = mapped_column("80212")
    original: Mapped[int] = mapped_column("80213")
    original_id_1: Mapped[str] = mapped_column("80201")
    original_id_2: Mapped[str] = mapped_column("80202")
    UNK_05: Mapped[str] = mapped_column("80221")
    UNK_06: Mapped[str] = mapped_column("80222")
    UNK_07: Mapped[int] = mapped_column("80021")
    UNK_08: Mapped[int] = mapped_column("80022")
    desc_1: Mapped[str] = mapped_column("80223")
    desc_2: Mapped[str] = mapped_column("80225")


@DatabaseManager.register_model("emoji")
class StickerPackage(Model):
    """
    market sticker package table
    emoji.db -> market_emoticon_package_table
    """
    __tablename__ = "market_emoticon_package_table"
    ID: Mapped[str] = mapped_column("80943", primary_key=True)
    UNK_01: Mapped[int] = mapped_column("80944")
    UNK_02: Mapped[str] = mapped_column("80945")
    UNK_03: Mapped[str] = mapped_column("80946")
    name: Mapped[str] = mapped_column("80947")
    desc: Mapped[str] = mapped_column("80948")
    UNK_04: Mapped[int] = mapped_column("80949")
    UNK_05: Mapped[str] = mapped_column("80950")
    UNK_06: Mapped[int] = mapped_column("80951")
    UNK_07: Mapped[int] = mapped_column("80952")
    UNK_08: Mapped[int] = mapped_column("80953")
    UNK_09: Mapped[int] = mapped_column("80954")
    UNK_10: Mapped[str] = mapped_column("80955")
    UNK_11: Mapped[int] = mapped_column("80956")
    UNK_12: Mapped[int] = mapped_column("80957")
    UNK_13: Mapped[int] = mapped_column("80958")
    UNK_14: Mapped[int] = mapped_column("80959")
    UNK_15: Mapped[int] = mapped_column("80960")
    UNK_16: Mapped[str] = mapped_column("80961")
    UNK_17: Mapped[int] = mapped_column("80962")
    UNK_18: Mapped[int] = mapped_column("80963")
    UNK_19: Mapped[int] = mapped_column("80964")
    UNK_20: Mapped[int] = mapped_column("80965")
    UNK_21: Mapped[int] = mapped_column("80966")
    UNK_21: Mapped[str] = mapped_column("80967")
    UNK_22: Mapped[int] = mapped_column("80968")
    UNK_23: Mapped[int] = mapped_column("80969")
    UNK_24: Mapped[str] = mapped_column("80970")
    UNK_25: Mapped[int] = mapped_column("80971")
    UNK_26: Mapped[str] = mapped_column("80972")
    UNK_27: Mapped[int] = mapped_column("80973")
    UNK_28: Mapped[int] = mapped_column("80974")


@DatabaseManager.register_model("emoji")
class StickerMapping(Model):
    """
    market sticker table
    emoji.db -> market_emoticon_table
    """
    __tablename__ = "market_emoticon_table"
    ID: Mapped[str] = mapped_column("80920", primary_key=True)
    pack_id: Mapped[str] = mapped_column("80943", primary_key=True)
    alt: Mapped[str] = mapped_column("80921")
    UNK_00: Mapped[str] = mapped_column("80922")  # always empty
    UNK_01: Mapped[int] = mapped_column("80923")  # always 0
    UNK_02: Mapped[int] = mapped_column("80924")  # always 200
    UNK_03: Mapped[int] = mapped_column("80925")  # always 200
    UNK_04: Mapped[int] = mapped_column("80926")  # always 0
    UNK_05: Mapped[str] = mapped_column("80927")  # always empty
    UNK_06: Mapped[int] = mapped_column("80928")  # always 2
    UNK_07: Mapped[str] = mapped_column("80929")  # always empty
    # keyword maybe used to fast type a sticker, always a list of two same elements
    keyword: Mapped[str] = mapped_column("80930")
    UNK_08: Mapped[str] = mapped_column("80931")  # always empty
    UNK_09: Mapped[int] = mapped_column("80932")  # always 0
    UNK_10: Mapped[int] = mapped_column("80933")  # always 0
    # protobuf, always b2c227095b20225b5d22205d0a, '[ "[]" ]'
    UNK_11: Mapped[bytes] = mapped_column("80934", LargeBinary)
    UNK_12: Mapped[int] = mapped_column("80935")  # always 0
    UNK_13: Mapped[str] = mapped_column("80936")  # always empty
    UNK_14: Mapped[str] = mapped_column("80937")  # always empty
    UNK_15: Mapped[int] = mapped_column("80938")  # always 0
    UNK_16: Mapped[int] = mapped_column("80939")  # always 0
    UNK_17: Mapped[int] = mapped_column("80940", nullable=True)  # always NULL
    UNK_18: Mapped[str] = mapped_column("80941")  # always empty
    UNK_19: Mapped[str] = mapped_column("80942")  # always empty
    UNK_20: Mapped[str] = mapped_column("80602", nullable=True)  # always NULL
    UNK_21: Mapped[str] = mapped_column("80603", nullable=True)  # always NULL
