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
        "CustomerPayPerConversionEligibilityFailureReasonEnum",
    },
)


class CustomerPayPerConversionEligibilityFailureReasonEnum(proto.Message):
    r"""Container for enum describing reasons why a customer is not
    eligible to use PaymentMode.CONVERSIONS.

    """

    class CustomerPayPerConversionEligibilityFailureReason(proto.Enum):
        r"""Enum describing possible reasons a customer is not eligible
        to use PaymentMode.CONVERSIONS.

        Values:
            UNSPECIFIED (0):
                Not specified.
            UNKNOWN (1):
                Used for return value only. Represents value
                unknown in this version.
            NOT_ENOUGH_CONVERSIONS (2):
                Customer does not have enough conversions.
            CONVERSION_LAG_TOO_HIGH (3):
                Customer's conversion lag is too high.
            HAS_CAMPAIGN_WITH_SHARED_BUDGET (4):
                Customer uses shared budgets.
            HAS_UPLOAD_CLICKS_CONVERSION (5):
                Customer has conversions with
                ConversionActionType.UPLOAD_CLICKS.
            AVERAGE_DAILY_SPEND_TOO_HIGH (6):
                Customer's average daily spend is too high.
            ANALYSIS_NOT_COMPLETE (7):
                Customer's eligibility has not yet been
                calculated by the Google Ads backend. Check back
                soon.
            OTHER (8):
                Customer is not eligible due to other
                reasons.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        NOT_ENOUGH_CONVERSIONS = 2
        CONVERSION_LAG_TOO_HIGH = 3
        HAS_CAMPAIGN_WITH_SHARED_BUDGET = 4
        HAS_UPLOAD_CLICKS_CONVERSION = 5
        AVERAGE_DAILY_SPEND_TOO_HIGH = 6
        ANALYSIS_NOT_COMPLETE = 7
        OTHER = 8


__all__ = tuple(sorted(__protobuf__.manifest))
