from odoo import models, fields


class PolishTest(models.Model):
    _name = 'polish.test'  # test model
    _description = 'Polish Test'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    abool = fields.Boolean(string='True or False')
    atext = fields.Text(string='Text')
    anhtml = fields.Html(string='Html')
    afloat = fields.Float(string='Float')
    adate = fields.Date(string='Data')
    adatetime = fields.Datetime(string='Date time')
    abin = fields.Binary()
    aselection = fields.Selection(selection=[('a', 'A'), ('b', 'B')])
    aref = fields.Reference([('polish_test', '')])
    arel_id = fields.Many2one('brat.polish.test')
    arel_ids = fields.One2many('brat.polish.test', 'arel_id')
    arels_ids = fields.Many2many('brat.polish.test')

