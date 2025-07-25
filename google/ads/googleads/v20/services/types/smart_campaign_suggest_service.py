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

from typing import MutableSequence

import proto  # type: ignore

from google.ads.googleads.v20.common.types import ad_type_infos
from google.ads.googleads.v20.common.types import criteria
from google.ads.googleads.v20.resources.types import (
    keyword_theme_constant as gagr_keyword_theme_constant,
)


__protobuf__ = proto.module(
    package="google.ads.googleads.v20.services",
    marshal="google.ads.googleads.v20",
    manifest={
        "SuggestSmartCampaignBudgetOptionsRequest",
        "SmartCampaignSuggestionInfo",
        "SuggestSmartCampaignBudgetOptionsResponse",
        "SuggestSmartCampaignAdRequest",
        "SuggestSmartCampaignAdResponse",
        "SuggestKeywordThemesRequest",
        "SuggestKeywordThemesResponse",
    },
)


class SuggestSmartCampaignBudgetOptionsRequest(proto.Message):
    r"""Request message for
    [SmartCampaignSuggestService.SuggestSmartCampaignBudgetOptions][google.ads.googleads.v20.services.SmartCampaignSuggestService.SuggestSmartCampaignBudgetOptions].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        customer_id (str):
            Required. The ID of the customer whose budget
            options are to be suggested.
        campaign (str):
            Required. The resource name of the campaign
            to get suggestion for.

            This field is a member of `oneof`_ ``suggestion_data``.
        suggestion_info (google.ads.googleads.v20.services.types.SmartCampaignSuggestionInfo):
            Required. Information needed to get budget
            options

            This field is a member of `oneof`_ ``suggestion_data``.
    """

    customer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    campaign: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="suggestion_data",
    )
    suggestion_info: "SmartCampaignSuggestionInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="suggestion_data",
        message="SmartCampaignSuggestionInfo",
    )


class SmartCampaignSuggestionInfo(proto.Message):
    r"""Information needed to get suggestion for Smart Campaign. More
    information provided will help the system to derive better
    suggestions.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        final_url (str):
            Optional. Landing page URL of the campaign.
        language_code (str):
            Optional. The two letter advertising language
            for the Smart campaign to be constructed,
            default to 'en' if not set.
        ad_schedules (MutableSequence[google.ads.googleads.v20.common.types.AdScheduleInfo]):
            Optional. The business ad schedule.
        keyword_themes (MutableSequence[google.ads.googleads.v20.common.types.KeywordThemeInfo]):
            Optional. Smart campaign keyword themes. This
            field may greatly improve suggestion accuracy
            and we recommend always setting it if possible.
        business_context (google.ads.googleads.v20.services.types.SmartCampaignSuggestionInfo.BusinessContext):
            Optional. Context describing the business to
            advertise.

            This field is a member of `oneof`_ ``business_setting``.
        business_profile_location (str):
            Optional. The resource name of a Business Profile location.
            Business Profile location resource names can be fetched
            through the Business Profile API and adhere to the following
            format: ``locations/{locationId}``.

            See the [Business Profile API]
            (https://developers.google.com/my-business/reference/businessinformation/rest/v1/accounts.locations)
            for additional details.

            This field is a member of `oneof`_ ``business_setting``.
        location_list (google.ads.googleads.v20.services.types.SmartCampaignSuggestionInfo.LocationList):
            Optional. The targeting geo location by
            locations.

            This field is a member of `oneof`_ ``geo_target``.
        proximity (google.ads.googleads.v20.common.types.ProximityInfo):
            Optional. The targeting geo location by
            proximity.

            This field is a member of `oneof`_ ``geo_target``.
    """

    class LocationList(proto.Message):
        r"""A list of locations.

        Attributes:
            locations (MutableSequence[google.ads.googleads.v20.common.types.LocationInfo]):
                Required. Locations.
        """

        locations: MutableSequence[criteria.LocationInfo] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=criteria.LocationInfo,
        )

    class BusinessContext(proto.Message):
        r"""A context that describes a business.

        Attributes:
            business_name (str):
                Optional. The name of the business.
        """

        business_name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    final_url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    ad_schedules: MutableSequence[criteria.AdScheduleInfo] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message=criteria.AdScheduleInfo,
        )
    )
    keyword_themes: MutableSequence[criteria.KeywordThemeInfo] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message=criteria.KeywordThemeInfo,
        )
    )
    business_context: BusinessContext = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="business_setting",
        message=BusinessContext,
    )
    business_profile_location: str = proto.Field(
        proto.STRING,
        number=9,
        oneof="business_setting",
    )
    location_list: LocationList = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="geo_target",
        message=LocationList,
    )
    proximity: criteria.ProximityInfo = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="geo_target",
        message=criteria.ProximityInfo,
    )


class SuggestSmartCampaignBudgetOptionsResponse(proto.Message):
    r"""Response message for
    [SmartCampaignSuggestService.SuggestSmartCampaignBudgetOptions][google.ads.googleads.v20.services.SmartCampaignSuggestService.SuggestSmartCampaignBudgetOptions].
    Depending on whether the system could suggest the options, either
    all of the options or none of them might be returned.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        low (google.ads.googleads.v20.services.types.SuggestSmartCampaignBudgetOptionsResponse.BudgetOption):
            Optional. The lowest budget option.

            This field is a member of `oneof`_ ``_low``.
        recommended (google.ads.googleads.v20.services.types.SuggestSmartCampaignBudgetOptionsResponse.BudgetOption):
            Optional. The recommended budget option.

            This field is a member of `oneof`_ ``_recommended``.
        high (google.ads.googleads.v20.services.types.SuggestSmartCampaignBudgetOptionsResponse.BudgetOption):
            Optional. The highest budget option.

            This field is a member of `oneof`_ ``_high``.
    """

    class Metrics(proto.Message):
        r"""Performance metrics for a given budget option.

        Attributes:
            min_daily_clicks (int):
                The estimated min daily clicks.
            max_daily_clicks (int):
                The estimated max daily clicks.
        """

        min_daily_clicks: int = proto.Field(
            proto.INT64,
            number=1,
        )
        max_daily_clicks: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class BudgetOption(proto.Message):
        r"""Smart Campaign budget option.

        Attributes:
            daily_amount_micros (int):
                The amount of the budget, in the local
                currency for the account. Amount is specified in
                micros, where one million is equivalent to one
                currency unit.
            metrics (google.ads.googleads.v20.services.types.SuggestSmartCampaignBudgetOptionsResponse.Metrics):
                Metrics pertaining to the suggested budget,
                could be empty if there is not enough
                information to derive the estimates.
        """

        daily_amount_micros: int = proto.Field(
            proto.INT64,
            number=1,
        )
        metrics: "SuggestSmartCampaignBudgetOptionsResponse.Metrics" = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                message="SuggestSmartCampaignBudgetOptionsResponse.Metrics",
            )
        )

    low: BudgetOption = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message=BudgetOption,
    )
    recommended: BudgetOption = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=BudgetOption,
    )
    high: BudgetOption = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=BudgetOption,
    )


class SuggestSmartCampaignAdRequest(proto.Message):
    r"""Request message for
    [SmartCampaignSuggestService.SuggestSmartCampaignAd][google.ads.googleads.v20.services.SmartCampaignSuggestService.SuggestSmartCampaignAd].

    Attributes:
        customer_id (str):
            Required. The ID of the customer.
        suggestion_info (google.ads.googleads.v20.services.types.SmartCampaignSuggestionInfo):
            Required. Inputs used to suggest a Smart campaign ad.
            Required fields: final_url, language_code, keyword_themes.
            Optional but recommended fields to improve the quality of
            the suggestion: business_setting and geo_target.
    """

    customer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    suggestion_info: "SmartCampaignSuggestionInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SmartCampaignSuggestionInfo",
    )


class SuggestSmartCampaignAdResponse(proto.Message):
    r"""Response message for
    [SmartCampaignSuggestService.SuggestSmartCampaignAd][google.ads.googleads.v20.services.SmartCampaignSuggestService.SuggestSmartCampaignAd].

    Attributes:
        ad_info (google.ads.googleads.v20.common.types.SmartCampaignAdInfo):
            Optional. Ad info includes 3 creative
            headlines and 2 creative descriptions.
    """

    ad_info: ad_type_infos.SmartCampaignAdInfo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=ad_type_infos.SmartCampaignAdInfo,
    )


class SuggestKeywordThemesRequest(proto.Message):
    r"""Request message for
    [SmartCampaignSuggestService.SuggestKeywordThemes][google.ads.googleads.v20.services.SmartCampaignSuggestService.SuggestKeywordThemes].

    Attributes:
        customer_id (str):
            Required. The ID of the customer.
        suggestion_info (google.ads.googleads.v20.services.types.SmartCampaignSuggestionInfo):
            Required. Information to get keyword theme suggestions.
            Required fields:

            -  suggestion_info.final_url
            -  suggestion_info.language_code
            -  suggestion_info.geo_target

            Recommended fields:

            -  suggestion_info.business_setting
    """

    customer_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    suggestion_info: "SmartCampaignSuggestionInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SmartCampaignSuggestionInfo",
    )


class SuggestKeywordThemesResponse(proto.Message):
    r"""Response message for
    [SmartCampaignSuggestService.SuggestKeywordThemes][google.ads.googleads.v20.services.SmartCampaignSuggestService.SuggestKeywordThemes].

    Attributes:
        keyword_themes (MutableSequence[google.ads.googleads.v20.services.types.SuggestKeywordThemesResponse.KeywordTheme]):
            Smart campaign keyword theme suggestions.
    """

    class KeywordTheme(proto.Message):
        r"""A Smart campaign keyword theme suggestion.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            keyword_theme_constant (google.ads.googleads.v20.resources.types.KeywordThemeConstant):
                A Smart campaign keyword theme constant.

                This field is a member of `oneof`_ ``keyword_theme``.
            free_form_keyword_theme (str):
                A free-form text keyword theme.

                This field is a member of `oneof`_ ``keyword_theme``.
        """

        keyword_theme_constant: (
            gagr_keyword_theme_constant.KeywordThemeConstant
        ) = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="keyword_theme",
            message=gagr_keyword_theme_constant.KeywordThemeConstant,
        )
        free_form_keyword_theme: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="keyword_theme",
        )

    keyword_themes: MutableSequence[KeywordTheme] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=KeywordTheme,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
