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

from google.ads.googleads.v20.enums.types import campaign_group_status


__protobuf__ = proto.module(
    package="google.ads.googleads.v20.resources",
    marshal="google.ads.googleads.v20",
    manifest={
        "CampaignGroup",
    },
)


class CampaignGroup(proto.Message):
    r"""A campaign group.

    Attributes:
        resource_name (str):
            Immutable. The resource name of the campaign group. Campaign
            group resource names have the form:

            ``customers/{customer_id}/campaignGroups/{campaign_group_id}``
        id (int):
            Output only. The ID of the campaign group.
        name (str):
            The name of the campaign group.

            This field is required and should not be empty
            when creating new campaign groups.

            It must not contain any null (code point 0x0),
            NL line feed (code point 0xA) or carriage return
            (code point 0xD) characters.
        status (google.ads.googleads.v20.enums.types.CampaignGroupStatusEnum.CampaignGroupStatus):
            The status of the campaign group.

            When a new campaign group is added, the status
            defaults to ENABLED.
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: int = proto.Field(
        proto.INT64,
        number=3,
    )
    name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status: (
        campaign_group_status.CampaignGroupStatusEnum.CampaignGroupStatus
    ) = proto.Field(
        proto.ENUM,
        number=5,
        enum=campaign_group_status.CampaignGroupStatusEnum.CampaignGroupStatus,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
