from odoo import models, fields, api


class Artists(models.Model):
    _name = 'artists'
    _description = 'Artists'

    name = fields.Char(string='Artist')
    month_listeners = fields.Integer(string='Month listeners')
    age = fields.Integer(string='Age')
    sex = fields.Char(string='Sex')
    country = fields.Char(string='Country')
    songs = fields.One2many('songs', 'author')

    def create_file_xml(self):
        return True
