# See LICENSE file for full copyright and licensing details.

{
    "name": "Account Voucher Report payment receipt",
    "version": "13.0.1.0.0",
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "maintainer": "Serpent Consulting Services Pvt. Ltd.",
    "website": "http://www.serpentcs.com",
    "license": "LGPL-3",
    "category": "Accounting & Finance",
    "summary": """
    Print payment receipt
    Payment receipt report
    Print voucher
    Print sales receipt
    Print purchase receipt
    Print customer receipt""",
    "description": """
    Print payment receipt
    Payment receipt report
    Print voucher
    Print sales receipt
    Print purchase receipt
    Print customer receipt
    Print supplier payment report
    payment report""",
    "depends": ['account'],
    "data": [
        'views/account_payment_view.xml',
        'views/res_company_views.xml',
        'views/report_configuration_view.xml',
        'report/account_payment_report.xml',
    ],
    "images": ['static/description/image.png'],
    "installable": True,
    "price": 12,
    "currency": "EUR",
}
