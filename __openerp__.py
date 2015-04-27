#-*- coding:utf-8 -*-
{
    'name': 'Benin - Payroll',
    'category': 'Localization',
    'author': 'ColourCog.com',
    'depends': [
        'hr_payroll',
    ],
    'version': '1.1',
    'description': """
Benin Payroll Rules.
======================
This module creates salary rules to handle Benin (bj) payroll.
Specifically this module allows companies to handle:
    * CNSS 
    * IPRR
    * AIB
    * VPS
    
This module also creates salary structures that incorporate these rules.
They may be used as-is, or as bases to location-specific rules.
    """,
    'data':[
        'l10n_bj_hr_payroll_data.xml',
        'l10n_bj_hr_payroll_view.xml',
    ],
    "installable": True,
    "auto_install": False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
