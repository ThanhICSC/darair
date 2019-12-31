# See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    is_remove_sign = fields.Boolean(string='Remove Sign', default=False)
