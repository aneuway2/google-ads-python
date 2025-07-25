# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations


import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.ads.googleads.v20.errors",
    marshal="google.ads.googleads.v20",
    manifest={
        "AssetSetLinkErrorEnum",
    },
)


class AssetSetLinkErrorEnum(proto.Message):
    r"""Container for enum describing possible asset set link errors."""

    class AssetSetLinkError(proto.Enum):
        r"""Enum describing possible asset set link errors.

        Values:
            UNSPECIFIED (0):
                Enum unspecified.
            UNKNOWN (1):
                The received error code is not known in this
                version.
            INCOMPATIBLE_ADVERTISING_CHANNEL_TYPE (2):
                Advertising channel type cannot be attached
                to the asset set due to channel-based
                restrictions.
            DUPLICATE_FEED_LINK (3):
                For this asset set type, only one campaign to
                feed linkage is allowed.
            INCOMPATIBLE_ASSET_SET_TYPE_WITH_CAMPAIGN_TYPE (4):
                The asset set type and campaign type are
                incompatible.
            DUPLICATE_ASSET_SET_LINK (5):
                Cannot link duplicate asset sets to the same
                campaign.
            ASSET_SET_LINK_CANNOT_BE_REMOVED (6):
                Cannot remove the asset set link. If a
                campaign is linked with only one asset set and
                you attempt to unlink them, this error will be
                triggered.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        INCOMPATIBLE_ADVERTISING_CHANNEL_TYPE = 2
        DUPLICATE_FEED_LINK = 3
        INCOMPATIBLE_ASSET_SET_TYPE_WITH_CAMPAIGN_TYPE = 4
        DUPLICATE_ASSET_SET_LINK = 5
        ASSET_SET_LINK_CANNOT_BE_REMOVED = 6


__all__ = tuple(sorted(__protobuf__.manifest))
