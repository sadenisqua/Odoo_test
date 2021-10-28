from odoo import models, fields, api


class Songs(models.Model):
    _name = 'songs'
    _description = 'Songs'

    name = fields.Char(string='Song name')
    duration = fields.Text(string='Duration')
    listeners = fields.Text(string='Listeners')
    author = fields.Many2one('artists')

    def create_file_xml(self):
        return True
