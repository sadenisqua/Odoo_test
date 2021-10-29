import xmltodict

from odoo import models, fields, api


class ParserXml(models.Model):
    _name = "parser"
    _description = "Parser Xml"

    xml_updater = fields.Binary(string='XML UPDATER')

    def parse_xml(self):
        return True
#     @staticmethod
#     def get_names():
#
#         with open("/home/user/Moduli/api_music/data/api_music.xml", "rb") as file:
#             result = xmltodict.parse(file)
#             # print(json.dumps(result))
#             artists_names = list(map(lambda artists: artists['name'], result['music']['Artists']['artist']))
#             artists_names_in_groups = []
#             for group in result['music']['Groups']['group']:
#                 for artist in group['artists']['artist']:
#                     artists_names_in_groups.append(artist['name'])
#             return artists_names, artists_names_in_groups
