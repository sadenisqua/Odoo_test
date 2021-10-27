from odoo import models, fields


class BratPolishTest(models.Model):
    _name = 'brat.polish.test'  # test model
    _description = 'Brat Polish Test'

    arel_id = fields.One2many('polish.test', 'arel_ids')
