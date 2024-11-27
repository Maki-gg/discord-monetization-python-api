from enum import IntEnum, StrEnum
from typing import Final


__all__: Final[tuple[str, ...]] = (
    "WebhookEventTypeEnum",
    "WebhookTypeEnum",
    "IntegrationTypeEnum",
    "EntitlementTypeEnum",
    "DiscordGuildNSFWLevelEnum",
    "DiscordGuildPremiumTierEnum",
    "DiscordGuildMFALevelEnum",
    "DiscordGuildExplicitContentFilterLevelEnum",
    "DiscordGuildDefaultMessageNotificationsLevelEnum",
    "DiscordGuildVerificationLevelEnum",
    "DiscordStickerTypeEnum",
    "DiscordStickerFormatTypeEnum",
)


class WebhookEventTypeEnum(StrEnum):
    APPLICATION_AUTHORIZED = "APPLICATION_AUTHORIZED"
    ENTITLEMENT_CREATE = "ENTITLEMENT_CREATE"
    QUEST_USER_ENROLLMENT = "QUEST_USER_ENROLLMENT"


class WebhookTypeEnum(IntEnum):
    PING = 0
    EVENT = 1


class IntegrationTypeEnum(IntEnum):
    GUILD_INSTALL = 0
    USER_INSTALL = 1


class EntitlementTypeEnum(IntEnum):
    PURCHASE = 1
    PREMIUM_SUBSCRIPTION = 2
    DEVELOPER_GIFT = 3
    TEST_MODE_PURCHASE = 4
    FREE_PURCHASE = 5
    USER_GIFT = 6
    PREMIUM_PURCHASE = 7
    APPLICATION_SUBSCRIPTION = 8


class DiscordGuildNSFWLevelEnum(IntEnum):
    DEFAULT = 0
    EXPLICIT = 1
    SAFE = 2
    AGE_RESTRICTED = 3


class DiscordGuildPremiumTierEnum(IntEnum):
    NONE = 0
    TIER_1 = 1
    TIER_2 = 2
    TIER_3 = 3


class DiscordGuildMFALevelEnum(IntEnum):
    NONE = 0
    ELEVATED = 1


class DiscordGuildExplicitContentFilterLevelEnum(IntEnum):
    DISABLED = 0
    MEMBERS_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2


class DiscordGuildDefaultMessageNotificationsLevelEnum(IntEnum):
    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1


class DiscordGuildVerificationLevelEnum(IntEnum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4


class DiscordStickerTypeEnum(IntEnum):
    STANDARD = 1
    GUILD = 2


class DiscordStickerFormatTypeEnum(IntEnum):
    PNG = 1
    APNG = 2
    LOTTIE = 3
    GIF = 4
