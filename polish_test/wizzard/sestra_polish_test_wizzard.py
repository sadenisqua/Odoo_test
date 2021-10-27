from odoo import models, fields, api


class SestraPolishTestWizzard(models.TransientModel):
    _name = 'sestra.polish.test.wizzard'
    # _inherit = 'res.partner'

    name = fields.Char()
    selection_type = fields.Selection(selection=[('person', 'Individual'), ('company', 'Company')])  # create
    wizzard_text = fields.Text()

    def wizzard_open(self):
        print('Click')
        return True

    def create_contact(self):
        if self.env['res.partner'].search([('name', '=', self.name)]):
            self.name = 'Change name'
        else:
            info = {
                'name': self.name,
                'company_type': self.selection_type,
                'is_wizzard': True
            }
            create_partner = self.env['res.partner'].create(info)
            return {"type": "ir.actions.act_window",
                    "res_model": "res.partner",
                    "view_mode": "form",
                    "target": "new",
                    "res_id": create_partner.id
                    }
