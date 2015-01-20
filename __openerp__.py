#-*- coding:utf-8 -*-
{
    'name': 'Benin - Payroll',
    'category': 'Localization',
    'author': 'ColourCog.com',
    'depends': [
        'hr_payroll',
    ],
    'version': '1.0',
    'description': """
Benin Payroll Rules.
======================

    * Employee Details
    * CNSS, IPTS, AIB, VPS
    
    TODO:
    * Generate Custom reports for social security and Fiscal Administration
    * Check and warn for missing Partner on employee (needed for vouchers)
    * Set default Payable Accounts for Payroll Partners
    * Automate payment voucher generation for Net payment
    * Create Bank/Cash Payment method  for voucher
    """,
    'data':[
        'l10n_bj_hr_payroll_view.xml',
        'l10n_bj_hr_payroll_data.xml',
    ],
    "installable": True,
    "auto_install": False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
