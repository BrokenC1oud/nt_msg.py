from sqlalchemy import LargeBinary, Text, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    ...


class PrivateMessage(Base):
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
    reply_body: Mapped[bytes] = mapped_column("40900", LargeBinary)  # protobuf, the message replied to
    UNK_19: Mapped[int] = mapped_column("40105")
    UNK_20: Mapped[int] = mapped_column("40005")
    timestamp_day: Mapped[int] = mapped_column("40058")  # time of the day the message was sent, in sec
    UNK_22: Mapped[int] = mapped_column("40006")
    UNK_23: Mapped[int] = mapped_column("40100")
    UNK_24: Mapped[bytes] = mapped_column("40600", LargeBinary)  # protobuf, seem to be related to reply, idk
    UNK_25: Mapped[int] = mapped_column("40060")
    UNK_26: Mapped[int] = mapped_column("40850")
    UNK_27: Mapped[int] = mapped_column("40851")
    UNK_28: Mapped[bytes] = mapped_column("40601", LargeBinary)  # always null
    UNK_29: Mapped[bytes] = mapped_column("40801", LargeBinary)  # protobuf
    UNK_30: Mapped[bytes] = mapped_column("40605", LargeBinary)  # protobuf, insufficient resource, related with file?
    contact_qq: Mapped[int] = mapped_column("40030")  # qq num
    sender_qq: Mapped[int] = mapped_column("40033")  # qq num
    UNK_33: Mapped[int] = mapped_column("40062")
    UNK_34: Mapped[int] = mapped_column("40083")
    UNK_35: Mapped[int] = mapped_column("40084")


class GroupMessage(Base):
    __tablename__ = "group_msg_table"
    ID: Mapped[int] = mapped_column("40001", primary_key=True)
    UNK_01: Mapped[int] = mapped_column("40002")
    seq: Mapped[int] = mapped_column("40003")
    UNK_03: Mapped[int] = mapped_column("40010")
    UNK_04: Mapped[int] = mapped_column("40011")
    UNK_05: Mapped[int] = mapped_column("40012")
    UNK_06: Mapped[int] = mapped_column("40013")
    group_id: Mapped[str] = mapped_column("40020", String(24))  # Tencent internal UID
    UNK_08: Mapped[int] = mapped_column("40026")
    group_qq: Mapped[str] = mapped_column("40021", String())  # Group qq
    group_qq_2: Mapped[int] = mapped_column("40027")  # group qq agn for no reason
    UNK_11: Mapped[int] = mapped_column("40040")
    UNK_12: Mapped[int] = mapped_column("40041")
    timestamp: Mapped[int] = mapped_column("40050")  # time message sent
    UNK_14: Mapped[int] = mapped_column("40052")
    UNK_15: Mapped[str] = mapped_column("40090", Text)  # empty
    nick_name: Mapped[str] = mapped_column("40093", Text)  # sender's nickname, not guaranteed (maybe empty)
    message_body: Mapped[bytes] = mapped_column("40800", LargeBinary)  # protobuf
    reply_body: Mapped[bytes] = mapped_column("40900", LargeBinary)  # protobuf, the message replied to
    UNK_19: Mapped[int] = mapped_column("40105")
    UNK_20: Mapped[int] = mapped_column("40005")
    timestamp_day: Mapped[int] = mapped_column("40058")  # time of the day the message was sent, in sec
    UNK_22: Mapped[int] = mapped_column("40006")
    UNK_23: Mapped[int] = mapped_column("40100")
    withdraw_status: Mapped[bytes] = mapped_column("40600", LargeBinary)  # protobuf, withdraw status
    UNK_25: Mapped[int] = mapped_column("40060")
    reply_to_seq: Mapped[int] = mapped_column("40850")  # seq of the message replying to
    UNK_27: Mapped[int] = mapped_column("40851")
    UNK_28: Mapped[bytes] = mapped_column("40601", LargeBinary)  # always null
    UNK_29: Mapped[bytes] = mapped_column("40801", LargeBinary)  # protobuf
    UNK_30: Mapped[bytes] = mapped_column("40605", LargeBinary)  # protobuf, insufficient resource, related with
                                                                            # file? always eae91300
    group_qq_3: Mapped[int] = mapped_column("40030")  # qq num
    sender_qq: Mapped[int] = mapped_column("40033")  # qq num
    UNK_33: Mapped[int] = mapped_column("40062")
    UNK_34: Mapped[int] = mapped_column("40083")
    UNK_35: Mapped[int] = mapped_column("40084")


class NTUIDMapping(Base):
    __tablename__ = "nt_uid_mapping_table"
    ID: Mapped[int] = mapped_column("48901", primary_key=True)
    uid: Mapped[str] = mapped_column("48902", String(24))
    UNK: Mapped[str] = mapped_column("48912", nullable=True)  # always null
    qq: Mapped[int] = mapped_column("1002")


engine = create_engine("sqlite:///./nt_msg.decrypt.db")
session = Session(engine)
