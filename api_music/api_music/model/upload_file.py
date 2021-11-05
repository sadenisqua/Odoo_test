from odoo import models, fields, api


class UploadFile(models.Model):
    _name = "upload.file"
    _description = "Parser Xml"

    xml_updater = fields.Binary(string='Import file xml', help='This is xml upload option.')
    xml_updater_name = fields.Char(string='File Name')

    def wizzard_start(self):

        return {"type": "ir.actions.act_window",
                "res_model": "upload.file.wizzard",
                "view_mode": "form",
                "target": "new",
                "context": {"default_import_xml": self.xml_updater,
                            "default_import_xml_name": self.xml_updater_name}
                }

