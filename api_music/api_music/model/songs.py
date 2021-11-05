from odoo import models, fields, api


class Songs(models.Model):
    _name = 'songs'
    _description = 'Songs'

    name = fields.Char(string='Song name')
    duration = fields.Text(string='Duration')
    listeners = fields.Text(string='Listeners')
    member = fields.Char(string='feat.')
    author = fields.Many2many('artists')
    groups = fields.Many2many('groups')
    albums_and_singles = fields.Many2many('albums.singles')
