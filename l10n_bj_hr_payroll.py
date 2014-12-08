#-*- coding:utf-8 -*-
from openerp.osv import fields, osv

import openerp.addons.decimal_precision as dp

class hr_employee_bj(osv.osv):
    _inherit = "hr.employee"

    _columns = {
        "cnss_number": fields.integer("CNSS number"),
        "ifu_number": fields.integer("IFU number"),
    }

hr_employee_bj()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
