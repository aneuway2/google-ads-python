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
        "SmartCampaignErrorEnum",
    },
)


class SmartCampaignErrorEnum(proto.Message):
    r"""Container for enum describing possible Smart campaign errors."""

    class SmartCampaignError(proto.Enum):
        r"""Enum describing possible Smart campaign errors.

        Values:
            UNSPECIFIED (0):
                Enum unspecified.
            UNKNOWN (1):
                The received error code is not known in this
                version.
            INVALID_BUSINESS_LOCATION_ID (2):
                The business location id is invalid.
            INVALID_CAMPAIGN (3):
                The SmartCampaignSetting resource is only
                applicable for campaigns with advertising
                channel type SMART.
            BUSINESS_NAME_OR_BUSINESS_LOCATION_ID_MISSING (4):
                The business name or business location id is
                required.
            REQUIRED_SUGGESTION_FIELD_MISSING (5):
                A Smart campaign suggestion request field is
                required.
            GEO_TARGETS_REQUIRED (6):
                A location list or proximity is required.
            CANNOT_DETERMINE_SUGGESTION_LOCALE (7):
                The locale could not be determined.
            FINAL_URL_NOT_CRAWLABLE (8):
                The final URL could not be crawled.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_BUSINESS_LOCATION_ID = 2
        INVALID_CAMPAIGN = 3
        BUSINESS_NAME_OR_BUSINESS_LOCATION_ID_MISSING = 4
        REQUIRED_SUGGESTION_FIELD_MISSING = 5
        GEO_TARGETS_REQUIRED = 6
        CANNOT_DETERMINE_SUGGESTION_LOCALE = 7
        FINAL_URL_NOT_CRAWLABLE = 8


__all__ = tuple(sorted(__protobuf__.manifest))
