from odoo import models, fields


class ContractsMyField(models.Model):

    _name = "res.partner"
    _inherit = ['res.partner']

    text = fields.Text(string='Sanya eto dlya tebya')
    is_wizzard = fields.Boolean(default=False)
