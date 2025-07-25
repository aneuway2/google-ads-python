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
    package="google.ads.googleads.v20.resources",
    marshal="google.ads.googleads.v20",
    manifest={
        "SmartCampaignSearchTermView",
    },
)


class SmartCampaignSearchTermView(proto.Message):
    r"""A Smart campaign search term view.

    Attributes:
        resource_name (str):
            Output only. The resource name of the Smart campaign search
            term view. Smart campaign search term view resource names
            have the form:

            ``customers/{customer_id}/smartCampaignSearchTermViews/{campaign_id}~{URL-base64_search_term}``
        search_term (str):
            Output only. The search term.
        campaign (str):
            Output only. The Smart campaign the search
            term served in.
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    search_term: str = proto.Field(
        proto.STRING,
        number=2,
    )
    campaign: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
