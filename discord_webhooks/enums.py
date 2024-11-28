"""
MIT License

Copyright (c) 2024-PRESENT Maki (https://maki.gg)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from enum import IntEnum, StrEnum
from typing import (
    Final,
    Literal,
    Tuple,
    Union,
)


__all__: Final[Tuple[str, ...]] = (
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
    "EntitlementTypeEnumLiterals",
    "DiscordStickerTypeEnumLiterals",
    "DiscordStickerFormatTypeEnumLiterals",
    "DiscordGuildVerificationLevelEnumLiterals",
    "DiscordGuildDefaultMessageNotificationsLevelEnumLiterals",
    "DiscordGuildExplicitContentFilterLevelEnumLiterals",
    "DiscordGuildMFALevelEnumLiterals",
    "DiscordGuildPremiumTierEnumLiterals",
    "DiscordGuildNSFWLevelEnumLiterals",
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


EntitlementTypeEnumLiterals = Union[
    Literal[EntitlementTypeEnum.PURCHASE],
    Literal[EntitlementTypeEnum.PREMIUM_SUBSCRIPTION],
    Literal[EntitlementTypeEnum.DEVELOPER_GIFT],
    Literal[EntitlementTypeEnum.TEST_MODE_PURCHASE],
    Literal[EntitlementTypeEnum.FREE_PURCHASE],
    Literal[EntitlementTypeEnum.USER_GIFT],
    Literal[EntitlementTypeEnum.PREMIUM_PURCHASE],
    Literal[EntitlementTypeEnum.APPLICATION_SUBSCRIPTION],
]


class DiscordGuildNSFWLevelEnum(IntEnum):
    DEFAULT = 0
    EXPLICIT = 1
    SAFE = 2
    AGE_RESTRICTED = 3


DiscordGuildNSFWLevelEnumLiterals = Union[
    Literal[DiscordGuildNSFWLevelEnum.DEFAULT],
    Literal[DiscordGuildNSFWLevelEnum.EXPLICIT],
    Literal[DiscordGuildNSFWLevelEnum.SAFE],
    Literal[DiscordGuildNSFWLevelEnum.AGE_RESTRICTED],
]


class DiscordGuildPremiumTierEnum(IntEnum):
    NONE = 0
    TIER_1 = 1
    TIER_2 = 2
    TIER_3 = 3


DiscordGuildPremiumTierEnumLiterals = Union[
    Literal[DiscordGuildPremiumTierEnum.NONE],
    Literal[DiscordGuildPremiumTierEnum.TIER_1],
    Literal[DiscordGuildPremiumTierEnum.TIER_2],
    Literal[DiscordGuildPremiumTierEnum.TIER_3],
]


class DiscordGuildMFALevelEnum(IntEnum):
    NONE = 0
    ELEVATED = 1


DiscordGuildMFALevelEnumLiterals = Union[
    Literal[DiscordGuildMFALevelEnum.NONE],
    Literal[DiscordGuildMFALevelEnum.ELEVATED],
]


class DiscordGuildExplicitContentFilterLevelEnum(IntEnum):
    DISABLED = 0
    MEMBERS_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2


DiscordGuildExplicitContentFilterLevelEnumLiterals = Union[
    Literal[DiscordGuildExplicitContentFilterLevelEnum.DISABLED],
    Literal[DiscordGuildExplicitContentFilterLevelEnum.MEMBERS_WITHOUT_ROLES],
    Literal[DiscordGuildExplicitContentFilterLevelEnum.ALL_MEMBERS],
]


class DiscordGuildDefaultMessageNotificationsLevelEnum(IntEnum):
    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1


DiscordGuildDefaultMessageNotificationsLevelEnumLiterals = Union[
    Literal[DiscordGuildDefaultMessageNotificationsLevelEnum.ALL_MESSAGES],
    Literal[DiscordGuildDefaultMessageNotificationsLevelEnum.ONLY_MENTIONS],
]


class DiscordGuildVerificationLevelEnum(IntEnum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4


DiscordGuildVerificationLevelEnumLiterals = Union[
    Literal[DiscordGuildVerificationLevelEnum.NONE],
    Literal[DiscordGuildVerificationLevelEnum.LOW],
    Literal[DiscordGuildVerificationLevelEnum.MEDIUM],
    Literal[DiscordGuildVerificationLevelEnum.HIGH],
    Literal[DiscordGuildVerificationLevelEnum.VERY_HIGH]
]


class DiscordStickerTypeEnum(IntEnum):
    STANDARD = 1
    GUILD = 2


DiscordStickerTypeEnumLiterals = Union[
    Literal[DiscordStickerTypeEnum.STANDARD],
    Literal[DiscordStickerTypeEnum.GUILD],
]


class DiscordStickerFormatTypeEnum(IntEnum):
    PNG = 1
    APNG = 2
    LOTTIE = 3
    GIF = 4


DiscordStickerFormatTypeEnumLiterals = Union[
    Literal[DiscordStickerFormatTypeEnum.PNG],
    Literal[DiscordStickerFormatTypeEnum.APNG],
    Literal[DiscordStickerFormatTypeEnum.LOTTIE],
    Literal[DiscordStickerFormatTypeEnum.GIF],
]
