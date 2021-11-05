from odoo import models, fields, api


class Artists(models.Model):
    _name = 'artists'
    _description = 'Artists'

    name = fields.Char(string='Artist')
    month_listeners = fields.Text(string='Month listeners')
    age = fields.Text(string='Age')
    sex = fields.Char(string='Sex')
    country = fields.Char(string='Country')
    songs = fields.Many2many('songs')
    groups = fields.Many2many('groups')
    albums_and_singles = fields.Many2many('albums.singles')
