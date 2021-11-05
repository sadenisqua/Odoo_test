from odoo import models, fields, api


class AlbumsSingles(models.Model):
    _name = 'albums.singles'
    _description = 'Albums and Singles'

    groups = fields.Many2many('groups')
    artists = fields.Many2many('artists')
    songs = fields.Many2many('songs')
    album_and_single = fields.Text(string='Albums and Singles')
