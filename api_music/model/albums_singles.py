from odoo import models, fields, api


class AlbumsSingles(models.Model):
    _name = 'albums.singles'
    _description = 'Albums and Singles'

    album_or_single = fields.Selection(selection=[('a', 'Album'), ('s', 'Single')])
    groups = fields.Many2many('groups')
    artists = fields.Many2many('artists')
    songs = fields.Many2many('songs')
