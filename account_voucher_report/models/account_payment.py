# See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    journal_type = fields.Selection(related='journal_id.type', string="Type")
    check_no = fields.Char(string='Check No.')
    reference = fields.Char(string='Payment Ref')

    def get_amount(self, amount):
        amt_en = self.currency_id.amount_to_text(amount)
        return amt_en
