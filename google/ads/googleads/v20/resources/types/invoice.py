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

from google.ads.googleads.v20.common.types import dates
from google.ads.googleads.v20.enums.types import invoice_type
from google.ads.googleads.v20.enums.types import month_of_year


__protobuf__ = proto.module(
    package="google.ads.googleads.v20.resources",
    marshal="google.ads.googleads.v20",
    manifest={
        "Invoice",
    },
)


class Invoice(proto.Message):
    r"""An invoice. All invoice information is snapshotted to match
    the PDF invoice. For invoices older than the launch of
    InvoiceService, the snapshotted information may not match the
    PDF invoice.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        resource_name (str):
            Output only. The resource name of the invoice. Multiple
            customers can share a given invoice, so multiple resource
            names may point to the same invoice. Invoice resource names
            have the form:

            ``customers/{customer_id}/invoices/{invoice_id}``
        id (str):
            Output only. The ID of the invoice. It
            appears on the invoice PDF as "Invoice number".

            This field is a member of `oneof`_ ``_id``.
        type_ (google.ads.googleads.v20.enums.types.InvoiceTypeEnum.InvoiceType):
            Output only. The type of invoice.
        billing_setup (str):
            Output only. The resource name of this invoice's billing
            setup.

            ``customers/{customer_id}/billingSetups/{billing_setup_id}``

            This field is a member of `oneof`_ ``_billing_setup``.
        payments_account_id (str):
            Output only. A 16 digit ID used to identify
            the payments account associated with the billing
            setup, for example, "1234-5678-9012-3456". It
            appears on the invoice PDF as "Billing Account
            Number".

            This field is a member of `oneof`_ ``_payments_account_id``.
        payments_profile_id (str):
            Output only. A 12 digit ID used to identify
            the payments profile associated with the billing
            setup, for example, "1234-5678-9012". It appears
            on the invoice PDF as "Billing ID".

            This field is a member of `oneof`_ ``_payments_profile_id``.
        issue_date (str):
            Output only. The issue date in yyyy-mm-dd
            format. It appears on the invoice PDF as either
            "Issue date" or "Invoice date".

            This field is a member of `oneof`_ ``_issue_date``.
        due_date (str):
            Output only. The due date in yyyy-mm-dd
            format.

            This field is a member of `oneof`_ ``_due_date``.
        service_date_range (google.ads.googleads.v20.common.types.DateRange):
            Output only. The service period date range of
            this invoice. The end date is inclusive.
        currency_code (str):
            Output only. The currency code. All costs are
            returned in this currency. A subset of the
            currency codes derived from the ISO 4217
            standard is supported.

            This field is a member of `oneof`_ ``_currency_code``.
        adjustments_subtotal_amount_micros (int):
            Output only. The pretax subtotal amount of
            invoice level adjustments, in micros.
        adjustments_tax_amount_micros (int):
            Output only. The sum of taxes on the invoice
            level adjustments, in micros.
        adjustments_total_amount_micros (int):
            Output only. The total amount of invoice
            level adjustments, in micros.
        regulatory_costs_subtotal_amount_micros (int):
            Output only. The pretax subtotal amount of
            invoice level regulatory costs, in micros.
        regulatory_costs_tax_amount_micros (int):
            Output only. The sum of taxes on the invoice
            level regulatory costs, in micros.
        regulatory_costs_total_amount_micros (int):
            Output only. The total amount of invoice
            level regulatory costs, in micros.
        export_charge_subtotal_amount_micros (int):
            Output only. The pretax subtotal amount of
            invoice level export charges, in micros.

            This field is a member of `oneof`_ ``_export_charge_subtotal_amount_micros``.
        export_charge_tax_amount_micros (int):
            Output only. The sum of taxes on the invoice
            level export charges, in micros.

            This field is a member of `oneof`_ ``_export_charge_tax_amount_micros``.
        export_charge_total_amount_micros (int):
            Output only. The total amount of invoice
            level export charges, in micros.

            This field is a member of `oneof`_ ``_export_charge_total_amount_micros``.
        subtotal_amount_micros (int):
            Output only. The pretax subtotal amount, in micros. This is
            equal to the sum of the AccountBudgetSummary subtotal
            amounts and Invoice.adjustments_subtotal_amount_micros.

            This field is a member of `oneof`_ ``_subtotal_amount_micros``.
        tax_amount_micros (int):
            Output only. The sum of all taxes on the
            invoice, in micros. This equals the sum of the
            AccountBudgetSummary tax amounts, plus taxes not
            associated with a specific account budget.

            This field is a member of `oneof`_ ``_tax_amount_micros``.
        total_amount_micros (int):
            Output only. The total amount, in micros. This equals the
            sum of Invoice.subtotal_amount_micros,
            Invoice.tax_amount_micros,
            Invoice.regulatory_costs_subtotal_amount_micros, and
            Invoice.export_charge_subtotal_amount_micros (which is
            separated into a separate line item starting with V14.1).

            This field is a member of `oneof`_ ``_total_amount_micros``.
        corrected_invoice (str):
            Output only. The resource name of the original invoice
            corrected, wrote off, or canceled by this invoice, if
            applicable. If ``corrected_invoice`` is set,
            ``replaced_invoices`` will not be set. Invoice resource
            names have the form:

            ``customers/{customer_id}/invoices/{invoice_id}``

            This field is a member of `oneof`_ ``_corrected_invoice``.
        replaced_invoices (MutableSequence[str]):
            Output only. The resource name of the original invoice(s)
            being rebilled or replaced by this invoice, if applicable.
            There might be multiple replaced invoices due to invoice
            consolidation. The replaced invoices may not belong to the
            same payments account. If ``replaced_invoices`` is set,
            ``corrected_invoice`` will not be set. Invoice resource
            names have the form:

            ``customers/{customer_id}/invoices/{invoice_id}``
        pdf_url (str):
            Output only. The URL to a PDF copy of the
            invoice. Users need to pass in their OAuth token
            to request the PDF with this URL.

            This field is a member of `oneof`_ ``_pdf_url``.
        account_budget_summaries (MutableSequence[google.ads.googleads.v20.resources.types.Invoice.AccountBudgetSummary]):
            Output only. The list of summarized account
            budget information associated with this invoice.
        account_summaries (MutableSequence[google.ads.googleads.v20.resources.types.Invoice.AccountSummary]):
            Output only. The list of summarized account
            information associated with this invoice.
    """

    class AccountSummary(proto.Message):
        r"""Represents a summarized view at account level.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            customer (str):
                Output only. The account associated with the
                account summary.

                This field is a member of `oneof`_ ``_customer``.
            billing_correction_subtotal_amount_micros (int):
                Output only. Pretax billing correction
                subtotal amount, in micros.

                This field is a member of `oneof`_ ``_billing_correction_subtotal_amount_micros``.
            billing_correction_tax_amount_micros (int):
                Output only. Tax on billing correction, in
                micros.

                This field is a member of `oneof`_ ``_billing_correction_tax_amount_micros``.
            billing_correction_total_amount_micros (int):
                Output only. Total billing correction amount,
                in micros.

                This field is a member of `oneof`_ ``_billing_correction_total_amount_micros``.
            coupon_adjustment_subtotal_amount_micros (int):
                Output only. Pretax coupon adjustment
                subtotal amount, in micros.

                This field is a member of `oneof`_ ``_coupon_adjustment_subtotal_amount_micros``.
            coupon_adjustment_tax_amount_micros (int):
                Output only. Tax on coupon adjustment, in
                micros.

                This field is a member of `oneof`_ ``_coupon_adjustment_tax_amount_micros``.
            coupon_adjustment_total_amount_micros (int):
                Output only. Total coupon adjustment amount,
                in micros.

                This field is a member of `oneof`_ ``_coupon_adjustment_total_amount_micros``.
            excess_credit_adjustment_subtotal_amount_micros (int):
                Output only. Pretax excess credit adjustment
                subtotal amount, in micros.

                This field is a member of `oneof`_ ``_excess_credit_adjustment_subtotal_amount_micros``.
            excess_credit_adjustment_tax_amount_micros (int):
                Output only. Tax on excess credit adjustment,
                in micros.

                This field is a member of `oneof`_ ``_excess_credit_adjustment_tax_amount_micros``.
            excess_credit_adjustment_total_amount_micros (int):
                Output only. Total excess credit adjustment
                amount, in micros.

                This field is a member of `oneof`_ ``_excess_credit_adjustment_total_amount_micros``.
            regulatory_costs_subtotal_amount_micros (int):
                Output only. Pretax regulatory costs subtotal
                amount, in micros.

                This field is a member of `oneof`_ ``_regulatory_costs_subtotal_amount_micros``.
            regulatory_costs_tax_amount_micros (int):
                Output only. Tax on regulatory costs, in
                micros.

                This field is a member of `oneof`_ ``_regulatory_costs_tax_amount_micros``.
            regulatory_costs_total_amount_micros (int):
                Output only. Total regulatory costs amount,
                in micros.

                This field is a member of `oneof`_ ``_regulatory_costs_total_amount_micros``.
            export_charge_subtotal_amount_micros (int):
                Output only. Pretax export charge subtotal
                amount, in micros.

                This field is a member of `oneof`_ ``_export_charge_subtotal_amount_micros``.
            export_charge_tax_amount_micros (int):
                Output only. Tax on export charge, in micros.

                This field is a member of `oneof`_ ``_export_charge_tax_amount_micros``.
            export_charge_total_amount_micros (int):
                Output only. Total export charge amount, in
                micros.

                This field is a member of `oneof`_ ``_export_charge_total_amount_micros``.
            subtotal_amount_micros (int):
                Output only. Total pretax subtotal amount
                attributable to the account during the service
                period, in micros.

                This field is a member of `oneof`_ ``_subtotal_amount_micros``.
            tax_amount_micros (int):
                Output only. Total tax amount attributable to
                the account during the service period, in
                micros.

                This field is a member of `oneof`_ ``_tax_amount_micros``.
            total_amount_micros (int):
                Output only. Total amount attributable to the account during
                the service period, in micros. This equals the sum of the
                subtotal_amount_micros and tax_amount_micros.

                This field is a member of `oneof`_ ``_total_amount_micros``.
        """

        customer: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        billing_correction_subtotal_amount_micros: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )
        billing_correction_tax_amount_micros: int = proto.Field(
            proto.INT64,
            number=3,
            optional=True,
        )
        billing_correction_total_amount_micros: int = proto.Field(
            proto.INT64,
            number=4,
            optional=True,
        )
        coupon_adjustment_subtotal_amount_micros: int = proto.Field(
            proto.INT64,
            number=5,
            optional=True,
        )
        coupon_adjustment_tax_amount_micros: int = proto.Field(
            proto.INT64,
            number=6,
            optional=True,
        )
        coupon_adjustment_total_amount_micros: int = proto.Field(
            proto.INT64,
            number=7,
            optional=True,
        )
        excess_credit_adjustment_subtotal_amount_micros: int = proto.Field(
            proto.INT64,
            number=8,
            optional=True,
        )
        excess_credit_adjustment_tax_amount_micros: int = proto.Field(
            proto.INT64,
            number=9,
            optional=True,
        )
        excess_credit_adjustment_total_amount_micros: int = proto.Field(
            proto.INT64,
            number=10,
            optional=True,
        )
        regulatory_costs_subtotal_amount_micros: int = proto.Field(
            proto.INT64,
            number=11,
            optional=True,
        )
        regulatory_costs_tax_amount_micros: int = proto.Field(
            proto.INT64,
            number=12,
            optional=True,
        )
        regulatory_costs_total_amount_micros: int = proto.Field(
            proto.INT64,
            number=13,
            optional=True,
        )
        export_charge_subtotal_amount_micros: int = proto.Field(
            proto.INT64,
            number=17,
            optional=True,
        )
        export_charge_tax_amount_micros: int = proto.Field(
            proto.INT64,
            number=18,
            optional=True,
        )
        export_charge_total_amount_micros: int = proto.Field(
            proto.INT64,
            number=19,
            optional=True,
        )
        subtotal_amount_micros: int = proto.Field(
            proto.INT64,
            number=14,
            optional=True,
        )
        tax_amount_micros: int = proto.Field(
            proto.INT64,
            number=15,
            optional=True,
        )
        total_amount_micros: int = proto.Field(
            proto.INT64,
            number=16,
            optional=True,
        )

    class AccountBudgetSummary(proto.Message):
        r"""Represents a summarized account budget billable cost.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            customer (str):
                Output only. The resource name of the customer associated
                with this account budget. This contains the customer ID,
                which appears on the invoice PDF as "Account ID". Customer
                resource names have the form:

                ``customers/{customer_id}``

                This field is a member of `oneof`_ ``_customer``.
            customer_descriptive_name (str):
                Output only. The descriptive name of the
                account budget's customer. It appears on the
                invoice PDF as "Account".

                This field is a member of `oneof`_ ``_customer_descriptive_name``.
            account_budget (str):
                Output only. The resource name of the account budget
                associated with this summarized billable cost. AccountBudget
                resource names have the form:

                ``customers/{customer_id}/accountBudgets/{account_budget_id}``

                This field is a member of `oneof`_ ``_account_budget``.
            account_budget_name (str):
                Output only. The name of the account budget.
                It appears on the invoice PDF as "Account
                budget".

                This field is a member of `oneof`_ ``_account_budget_name``.
            purchase_order_number (str):
                Output only. The purchase order number of the
                account budget. It appears on the invoice PDF as
                "Purchase order".

                This field is a member of `oneof`_ ``_purchase_order_number``.
            subtotal_amount_micros (int):
                Output only. The pretax subtotal amount
                attributable to this budget during the service
                period, in micros.

                This field is a member of `oneof`_ ``_subtotal_amount_micros``.
            tax_amount_micros (int):
                Output only. The tax amount attributable to
                this budget during the service period, in
                micros.

                This field is a member of `oneof`_ ``_tax_amount_micros``.
            total_amount_micros (int):
                Output only. The total amount attributable to
                this budget during the service period, in
                micros. This equals the sum of the account
                budget subtotal amount and the account budget
                tax amount.

                This field is a member of `oneof`_ ``_total_amount_micros``.
            billable_activity_date_range (google.ads.googleads.v20.common.types.DateRange):
                Output only. The billable activity date range
                of the account budget, within the service date
                range of this invoice. The end date is
                inclusive. This can be different from the
                account budget's start and end time.
            served_amount_micros (int):
                Output only. The pretax served amount
                attributable to this budget during the service
                period, in micros. This is only useful to
                reconcile invoice and delivery data.

                This field is a member of `oneof`_ ``_served_amount_micros``.
            billed_amount_micros (int):
                Output only. The pretax billed amount
                attributable to this budget during the service
                period, in micros. This does not account for any
                adjustments.

                This field is a member of `oneof`_ ``_billed_amount_micros``.
            overdelivery_amount_micros (int):
                Output only. The pretax overdelivery amount
                attributable to this budget during the service
                period, in micros (negative value).

                This field is a member of `oneof`_ ``_overdelivery_amount_micros``.
            invalid_activity_amount_micros (int):
                Output only. The pretax invalid activity
                amount attributable to this budget in previous
                months, in micros (negative value).

                This field is a member of `oneof`_ ``_invalid_activity_amount_micros``.
            invalid_activity_summaries (MutableSequence[google.ads.googleads.v20.resources.types.Invoice.InvalidActivitySummary]):
                Output only. The list of summarized invalid
                activity credits with original linkages.
        """

        customer: str = proto.Field(
            proto.STRING,
            number=10,
            optional=True,
        )
        customer_descriptive_name: str = proto.Field(
            proto.STRING,
            number=11,
            optional=True,
        )
        account_budget: str = proto.Field(
            proto.STRING,
            number=12,
            optional=True,
        )
        account_budget_name: str = proto.Field(
            proto.STRING,
            number=13,
            optional=True,
        )
        purchase_order_number: str = proto.Field(
            proto.STRING,
            number=14,
            optional=True,
        )
        subtotal_amount_micros: int = proto.Field(
            proto.INT64,
            number=15,
            optional=True,
        )
        tax_amount_micros: int = proto.Field(
            proto.INT64,
            number=16,
            optional=True,
        )
        total_amount_micros: int = proto.Field(
            proto.INT64,
            number=17,
            optional=True,
        )
        billable_activity_date_range: dates.DateRange = proto.Field(
            proto.MESSAGE,
            number=9,
            message=dates.DateRange,
        )
        served_amount_micros: int = proto.Field(
            proto.INT64,
            number=18,
            optional=True,
        )
        billed_amount_micros: int = proto.Field(
            proto.INT64,
            number=19,
            optional=True,
        )
        overdelivery_amount_micros: int = proto.Field(
            proto.INT64,
            number=20,
            optional=True,
        )
        invalid_activity_amount_micros: int = proto.Field(
            proto.INT64,
            number=21,
            optional=True,
        )
        invalid_activity_summaries: MutableSequence[
            "Invoice.InvalidActivitySummary"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=22,
            message="Invoice.InvalidActivitySummary",
        )

    class InvalidActivitySummary(proto.Message):
        r"""Details about the invalid activity for the invoice that
        contain additional details about invoice against which
        corrections are made.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            original_month_of_service (google.ads.googleads.v20.enums.types.MonthOfYearEnum.MonthOfYear):
                Output only. Original month of service
                related to this invalid activity credit.

                This field is a member of `oneof`_ ``_original_month_of_service``.
            original_year_of_service (str):
                Output only. Original year of service related
                to this invalid activity credit.

                This field is a member of `oneof`_ ``_original_year_of_service``.
            original_invoice_id (str):
                Output only. Original invoice number related
                to this invalid activity credit.

                This field is a member of `oneof`_ ``_original_invoice_id``.
            original_account_budget_name (str):
                Output only. Original account budget name
                related to this invalid activity credit.

                This field is a member of `oneof`_ ``_original_account_budget_name``.
            original_purchase_order_number (str):
                Output only. Original purchase order number
                related to this invalid activity credit.

                This field is a member of `oneof`_ ``_original_purchase_order_number``.
            amount_micros (int):
                Output only. Invalid activity amount in
                micros.

                This field is a member of `oneof`_ ``_amount_micros``.
        """

        original_month_of_service: month_of_year.MonthOfYearEnum.MonthOfYear = (
            proto.Field(
                proto.ENUM,
                number=1,
                optional=True,
                enum=month_of_year.MonthOfYearEnum.MonthOfYear,
            )
        )
        original_year_of_service: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )
        original_invoice_id: str = proto.Field(
            proto.STRING,
            number=3,
            optional=True,
        )
        original_account_budget_name: str = proto.Field(
            proto.STRING,
            number=4,
            optional=True,
        )
        original_purchase_order_number: str = proto.Field(
            proto.STRING,
            number=5,
            optional=True,
        )
        amount_micros: int = proto.Field(
            proto.INT64,
            number=6,
            optional=True,
        )

    resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=25,
        optional=True,
    )
    type_: invoice_type.InvoiceTypeEnum.InvoiceType = proto.Field(
        proto.ENUM,
        number=3,
        enum=invoice_type.InvoiceTypeEnum.InvoiceType,
    )
    billing_setup: str = proto.Field(
        proto.STRING,
        number=26,
        optional=True,
    )
    payments_account_id: str = proto.Field(
        proto.STRING,
        number=27,
        optional=True,
    )
    payments_profile_id: str = proto.Field(
        proto.STRING,
        number=28,
        optional=True,
    )
    issue_date: str = proto.Field(
        proto.STRING,
        number=29,
        optional=True,
    )
    due_date: str = proto.Field(
        proto.STRING,
        number=30,
        optional=True,
    )
    service_date_range: dates.DateRange = proto.Field(
        proto.MESSAGE,
        number=9,
        message=dates.DateRange,
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=31,
        optional=True,
    )
    adjustments_subtotal_amount_micros: int = proto.Field(
        proto.INT64,
        number=19,
    )
    adjustments_tax_amount_micros: int = proto.Field(
        proto.INT64,
        number=20,
    )
    adjustments_total_amount_micros: int = proto.Field(
        proto.INT64,
        number=21,
    )
    regulatory_costs_subtotal_amount_micros: int = proto.Field(
        proto.INT64,
        number=22,
    )
    regulatory_costs_tax_amount_micros: int = proto.Field(
        proto.INT64,
        number=23,
    )
    regulatory_costs_total_amount_micros: int = proto.Field(
        proto.INT64,
        number=24,
    )
    export_charge_subtotal_amount_micros: int = proto.Field(
        proto.INT64,
        number=40,
        optional=True,
    )
    export_charge_tax_amount_micros: int = proto.Field(
        proto.INT64,
        number=41,
        optional=True,
    )
    export_charge_total_amount_micros: int = proto.Field(
        proto.INT64,
        number=42,
        optional=True,
    )
    subtotal_amount_micros: int = proto.Field(
        proto.INT64,
        number=33,
        optional=True,
    )
    tax_amount_micros: int = proto.Field(
        proto.INT64,
        number=34,
        optional=True,
    )
    total_amount_micros: int = proto.Field(
        proto.INT64,
        number=35,
        optional=True,
    )
    corrected_invoice: str = proto.Field(
        proto.STRING,
        number=36,
        optional=True,
    )
    replaced_invoices: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=37,
    )
    pdf_url: str = proto.Field(
        proto.STRING,
        number=38,
        optional=True,
    )
    account_budget_summaries: MutableSequence[AccountBudgetSummary] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=18,
            message=AccountBudgetSummary,
        )
    )
    account_summaries: MutableSequence[AccountSummary] = proto.RepeatedField(
        proto.MESSAGE,
        number=39,
        message=AccountSummary,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
