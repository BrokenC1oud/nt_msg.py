from .models import *

_models = {
    "nt_msg": [
        PrivateMessage,
        GroupMessage,
        NTUIDMapping,
    ],
    "emoji": [
        SystemEmoji,
        BottomEmoji,
        EmojiConfig,
        EmojiGroup,
        EmojiMiscData,
        FavEmojiInfo,
        StickerPackage,
        StickerMapping,
    ],
    "group_info": [
        DoubtGroupNotifyList,
        GroupBulletin,
        GroupDetailInfo,
        GroupEssence,
        GroupList,
        GroupMember,
        GroupLevelBadge,
        GroupNotify,
    ],
    "profile_info": [
        Buddy,
        BuddyRequest,
        BuddyCategory,
        BotProfile,
        BuddyProfile,
    ]
}

class DatabaseManager:
    ...
