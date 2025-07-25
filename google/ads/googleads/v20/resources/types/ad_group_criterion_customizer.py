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

from google.ads.googleads.v20.common.types import customizer_value
from google.ads.googleads.v20.enums.types import customizer_value_status


__protobuf__ = proto.module(
    package="google.ads.googleads.v20.resources",
    marshal="google.ads.googleads.v20",
    manifest={
        "AdGroupCriterionCustomizer",
    },
)


class AdGroupCriterionCustomizer(proto.Message):
    r"""A customizer value for the associated CustomizerAttribute at
    the AdGroupCriterion level.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        resource_name (str):
            Immutable. The resource name of the ad group criterion
            customizer. Ad group criterion customizer resource names
            have the form:

            ``customers/{customer_id}/adGroupCriterionCustomizers/{ad_group_id}~{criterion_id}~{customizer_attribute_id}``
        ad_group_criterion (str):
            Immutable. The ad group criterion to which
            the customizer attribute is linked. It must be a
            keyword criterion.

            This field is a member of `oneof`_ ``_ad_group_criterion``.
        customizer_attribute (str):
            Required. Immutable. The customizer attribute
            which is linked to the ad group criterion.
        status (google.ads.googleads.v20.enums.types.CustomizerValueStatusEnum.CustomizerValueStatus):
            Output only. The status of the ad group
            criterion customizer.
        value (google.ads.googleads.v20.common.types.CustomizerValue):
            Required. The value to associate with the
            customizer attribute at this level. The value
            must be of the type specified for the
            CustomizerAttribute.
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ad_group_criterion: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    customizer_attribute: str = proto.Field(
        proto.STRING,
        number=3,
    )
    status: (
        customizer_value_status.CustomizerValueStatusEnum.CustomizerValueStatus
    ) = proto.Field(
        proto.ENUM,
        number=4,
        enum=customizer_value_status.CustomizerValueStatusEnum.CustomizerValueStatus,
    )
    value: customizer_value.CustomizerValue = proto.Field(
        proto.MESSAGE,
        number=5,
        message=customizer_value.CustomizerValue,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
