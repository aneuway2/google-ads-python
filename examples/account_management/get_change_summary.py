#!/usr/bin/env python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example gets a list of which resources have been changed in an account."""


import argparse
import sys

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
from google.ads.googleads.v20.services.services.google_ads_service.client import (
    GoogleAdsServiceClient,
)
from google.ads.googleads.v20.services.types.google_ads_service import (
    SearchGoogleAdsRequest,
    SearchPagedResponse,
    GoogleAdsRow,
)
from google.ads.googleads.v20.resources.types.change_status import ChangeStatus


# [START get_change_summary]
def main(client: GoogleAdsClient, customer_id: str) -> None:
    ads_service: GoogleAdsServiceClient = client.get_service("GoogleAdsService")

    # Construct a query to find information about changed resources in your
    # account.
    query = """
        SELECT
          change_status.resource_name,
          change_status.last_change_date_time,
          change_status.resource_type,
          change_status.campaign,
          change_status.ad_group,
          change_status.resource_status,
          change_status.ad_group_ad,
          change_status.ad_group_criterion,
          change_status.campaign_criterion
        FROM change_status
        WHERE change_status.last_change_date_time DURING LAST_14_DAYS
        ORDER BY change_status.last_change_date_time
        LIMIT 10000"""

    search_request: SearchGoogleAdsRequest = client.get_type(
        "SearchGoogleAdsRequest"
    )
    search_request.customer_id = customer_id
    search_request.query = query

    response: SearchPagedResponse = ads_service.search(request=search_request)

    row: GoogleAdsRow
    for row in response:
        cs: ChangeStatus = row.change_status
        resource_type: str = cs.resource_type.name
        resource_name: str
        if resource_type == "AD_GROUP":
            resource_name = cs.ad_group
        elif resource_type == "AD_GROUP_AD":
            resource_name = cs.ad_group_ad
        elif resource_type == "AD_GROUP_CRITERION":
            resource_name = cs.ad_group_criterion
        elif resource_type == "CAMPAIGN":
            resource_name = cs.campaign
        elif resource_type == "CAMPAIGN_CRITERION":
            resource_name = cs.campaign_criterion
        else:
            resource_name = "UNKNOWN"

        resource_status: str = cs.resource_status.name
        print(
            f"On '{cs.last_change_date_time}', change status "
            f"'{cs.resource_name}' shows that a resource type of "
            f"'{resource_type}' with resource name '{resource_name}' was "
            f"{resource_status}"
        )
        # [END get_change_summary]


if __name__ == "__main__":
    # GoogleAdsClient will read a google-ads.yaml configuration file in the
    parser = argparse.ArgumentParser(
        description=(
            "Displays account changes that occurred in the last 7 days."
        )
    )
    # The following argument(s) should be provided to run the example.
    parser.add_argument(
        "-c",
        "--customer_id",
        type=str,
        required=True,
        help="The Google Ads customer ID.",
    )
    args = parser.parse_args()

    # GoogleAdsClient will read the google-ads.yaml configuration file in the
    # home directory if none is specified.
    googleads_client = GoogleAdsClient.load_from_storage(version="v20")

    try:
        main(googleads_client, args.customer_id)
    except GoogleAdsException as ex:
        print(
            f'Request with ID "{ex.request_id}" failed with status '
            f'"{ex.error.code().name}" and includes the following errors:'
        )
        for error in ex.failure.errors:
            print(f'\tError with message "{error.message}".')
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f"\t\tOn field: {field_path_element.field_name}")
        sys.exit(1)
