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
    package="google.ads.googleads.v20.enums",
    marshal="google.ads.googleads.v20",
    manifest={
        "CampaignPrimaryStatusReasonEnum",
    },
)


class CampaignPrimaryStatusReasonEnum(proto.Message):
    r"""Container for enum describing possible campaign primary
    status reasons.

    """

    class CampaignPrimaryStatusReason(proto.Enum):
        r"""Enum describing the possible campaign primary status reasons.
        Provides insight into why a campaign is not serving or not
        serving optimally. These reasons are aggregated to determine an
        overall campaign primary status.

        Values:
            UNSPECIFIED (0):
                Not specified.
            UNKNOWN (1):
                Used for return value only. Represents value
                unknown in this version.
            CAMPAIGN_REMOVED (2):
                The user-specified campaign status is
                removed.
            CAMPAIGN_PAUSED (3):
                The user-specified campaign status is paused.
            CAMPAIGN_PENDING (4):
                The user-specified time for this campaign to
                start is in the future.
            CAMPAIGN_ENDED (5):
                The user-specified time for this campaign to
                end has passed.
            CAMPAIGN_DRAFT (6):
                The campaign is a draft.
            BIDDING_STRATEGY_MISCONFIGURED (7):
                The bidding strategy has incorrect
                user-specified settings.
            BIDDING_STRATEGY_LIMITED (8):
                The bidding strategy is limited by
                user-specified settings such as lack of data or
                similar.
            BIDDING_STRATEGY_LEARNING (9):
                The automated bidding system is adjusting to
                user-specified changes to the bidding strategy.
            BIDDING_STRATEGY_CONSTRAINED (10):
                Campaign could capture more conversion value
                by adjusting CPA/ROAS targets.
            BUDGET_CONSTRAINED (11):
                The budget is limiting the campaign's ability
                to serve.
            BUDGET_MISCONFIGURED (12):
                The budget has incorrect user-specified
                settings.
            SEARCH_VOLUME_LIMITED (13):
                Campaign is not targeting all relevant
                queries.
            AD_GROUPS_PAUSED (14):
                The user-specified ad group statuses are all
                paused.
            NO_AD_GROUPS (15):
                No eligible ad groups exist in this campaign.
            KEYWORDS_PAUSED (16):
                The user-specified keyword statuses are all
                paused.
            NO_KEYWORDS (17):
                No eligible keywords exist in this campaign.
            AD_GROUP_ADS_PAUSED (18):
                The user-specified ad group ad statuses are
                all paused.
            NO_AD_GROUP_ADS (19):
                No eligible ad group ads exist in this
                campaign.
            HAS_ADS_LIMITED_BY_POLICY (20):
                At least one ad in this campaign is limited
                by policy.
            HAS_ADS_DISAPPROVED (21):
                At least one ad in this campaign is
                disapproved.
            MOST_ADS_UNDER_REVIEW (22):
                Most ads in this campaign are pending review.
            MISSING_LEAD_FORM_EXTENSION (23):
                The campaign has a lead form goal, and the
                lead form extension is missing.
            MISSING_CALL_EXTENSION (24):
                The campaign has a call goal, and the call
                extension is missing.
            LEAD_FORM_EXTENSION_UNDER_REVIEW (25):
                The lead form extension is under review.
            LEAD_FORM_EXTENSION_DISAPPROVED (26):
                The lead extension is disapproved.
            CALL_EXTENSION_UNDER_REVIEW (27):
                The call extension is under review.
            CALL_EXTENSION_DISAPPROVED (28):
                The call extension is disapproved.
            NO_MOBILE_APPLICATION_AD_GROUP_CRITERIA (29):
                No eligible mobile application ad group
                criteria exist in this campaign.
            CAMPAIGN_GROUP_PAUSED (30):
                The user-specified campaign group status is
                paused.
            CAMPAIGN_GROUP_ALL_GROUP_BUDGETS_ENDED (31):
                The user-specified times of all group budgets
                associated with the parent campaign group has
                passed.
            APP_NOT_RELEASED (32):
                The app associated with this ACi campaign is
                not released in the target countries of the
                campaign.
            APP_PARTIALLY_RELEASED (33):
                The app associated with this ACi campaign is
                partially released in the target countries of
                the campaign.
            HAS_ASSET_GROUPS_DISAPPROVED (34):
                At least one asset group in this campaign is
                disapproved.
            HAS_ASSET_GROUPS_LIMITED_BY_POLICY (35):
                At least one asset group in this campaign is
                limited by policy.
            MOST_ASSET_GROUPS_UNDER_REVIEW (36):
                Most asset groups in this campaign are
                pending review.
            NO_ASSET_GROUPS (37):
                No eligible asset groups exist in this
                campaign.
            ASSET_GROUPS_PAUSED (38):
                All asset groups in this campaign are paused.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        CAMPAIGN_REMOVED = 2
        CAMPAIGN_PAUSED = 3
        CAMPAIGN_PENDING = 4
        CAMPAIGN_ENDED = 5
        CAMPAIGN_DRAFT = 6
        BIDDING_STRATEGY_MISCONFIGURED = 7
        BIDDING_STRATEGY_LIMITED = 8
        BIDDING_STRATEGY_LEARNING = 9
        BIDDING_STRATEGY_CONSTRAINED = 10
        BUDGET_CONSTRAINED = 11
        BUDGET_MISCONFIGURED = 12
        SEARCH_VOLUME_LIMITED = 13
        AD_GROUPS_PAUSED = 14
        NO_AD_GROUPS = 15
        KEYWORDS_PAUSED = 16
        NO_KEYWORDS = 17
        AD_GROUP_ADS_PAUSED = 18
        NO_AD_GROUP_ADS = 19
        HAS_ADS_LIMITED_BY_POLICY = 20
        HAS_ADS_DISAPPROVED = 21
        MOST_ADS_UNDER_REVIEW = 22
        MISSING_LEAD_FORM_EXTENSION = 23
        MISSING_CALL_EXTENSION = 24
        LEAD_FORM_EXTENSION_UNDER_REVIEW = 25
        LEAD_FORM_EXTENSION_DISAPPROVED = 26
        CALL_EXTENSION_UNDER_REVIEW = 27
        CALL_EXTENSION_DISAPPROVED = 28
        NO_MOBILE_APPLICATION_AD_GROUP_CRITERIA = 29
        CAMPAIGN_GROUP_PAUSED = 30
        CAMPAIGN_GROUP_ALL_GROUP_BUDGETS_ENDED = 31
        APP_NOT_RELEASED = 32
        APP_PARTIALLY_RELEASED = 33
        HAS_ASSET_GROUPS_DISAPPROVED = 34
        HAS_ASSET_GROUPS_LIMITED_BY_POLICY = 35
        MOST_ASSET_GROUPS_UNDER_REVIEW = 36
        NO_ASSET_GROUPS = 37
        ASSET_GROUPS_PAUSED = 38


__all__ = tuple(sorted(__protobuf__.manifest))
