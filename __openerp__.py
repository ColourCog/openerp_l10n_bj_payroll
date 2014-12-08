#-*- coding:utf-8 -*-
{
    'name': 'Benin - Payroll',
    'category': 'Localization',
    'author': 'OpenERP SA',
    'depends': ['hr_payroll'],
    'version': '1.0',
    'description': """
Benin Payroll Rules.
======================

    * Employee Details
    * Allowances/Deductions
    * Employee Payslip
    * Integrated with Holiday Management
    * CNSS, IPTS, AIB
    """,
    'data':[
        'l10n_bj_hr_payroll_view.xml',
        'l10n_bj_hr_payroll_data.xml',
    ],
    "installable": True,
    "auto_install": False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
