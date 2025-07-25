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
        "AccessReasonEnum",
    },
)


class AccessReasonEnum(proto.Message):
    r"""Indicates the way the resource such as user list is related
    to a user.

    """

    class AccessReason(proto.Enum):
        r"""Enum describing possible access reasons.

        Values:
            UNSPECIFIED (0):
                Not specified.
            UNKNOWN (1):
                Used for return value only. Represents value
                unknown in this version.
            OWNED (2):
                The resource is owned by the user.
            SHARED (3):
                The resource is shared to the user.
            LICENSED (4):
                The resource is licensed to the user.
            SUBSCRIBED (5):
                The user subscribed to the resource.
            AFFILIATED (6):
                The resource is accessible to the user.
        """

        UNSPECIFIED = 0
        UNKNOWN = 1
        OWNED = 2
        SHARED = 3
        LICENSED = 4
        SUBSCRIBED = 5
        AFFILIATED = 6


__all__ = tuple(sorted(__protobuf__.manifest))
