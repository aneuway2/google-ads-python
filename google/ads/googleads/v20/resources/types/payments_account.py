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
        "PaymentsAccount",
    },
)


class PaymentsAccount(proto.Message):
    r"""A payments account, which can be used to set up billing for
    an Ads customer.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        resource_name (str):
            Output only. The resource name of the payments account.
            PaymentsAccount resource names have the form:

            ``customers/{customer_id}/paymentsAccounts/{payments_account_id}``
        payments_account_id (str):
            Output only. A 16 digit ID used to identify a
            payments account.

            This field is a member of `oneof`_ ``_payments_account_id``.
        name (str):
            Output only. The name of the payments
            account.

            This field is a member of `oneof`_ ``_name``.
        currency_code (str):
            Output only. The currency code of the
            payments account. A subset of the currency codes
            derived from the ISO 4217 standard is supported.

            This field is a member of `oneof`_ ``_currency_code``.
        payments_profile_id (str):
            Output only. A 12 digit ID used to identify
            the payments profile associated with the
            payments account.

            This field is a member of `oneof`_ ``_payments_profile_id``.
        secondary_payments_profile_id (str):
            Output only. A secondary payments profile ID
            present in uncommon situations, for example,
            when a sequential liability agreement has been
            arranged.

            This field is a member of `oneof`_ ``_secondary_payments_profile_id``.
        paying_manager_customer (str):
            Output only. Paying manager of this payment
            account.

            This field is a member of `oneof`_ ``_paying_manager_customer``.
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    payments_account_id: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    name: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    payments_profile_id: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    secondary_payments_profile_id: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    paying_manager_customer: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
