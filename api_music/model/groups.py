from odoo import models, fields, api


class Groups(models.Model):
    _name = 'groups'
    _description = 'Groups'

    name = fields.Char(string='Name')
    month_listeners = fields.Integer(string='Month listeners')
    songs = fields.One2many('songs', 'author')
    artists = fields.One2many('artists', 'name')

    def create_file_xml(self):
        return True
