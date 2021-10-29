from odoo import models, fields, api


class Groups(models.Model):
    _name = 'groups'
    _description = 'Groups'

    name = fields.Char(string='Name')
    month_listeners = fields.Text(string='Month listeners')
    songs = fields.Many2many('songs')
    artists = fields.Many2many('artists')
    albums_and_singles = fields.Many2many('albums.singles')
