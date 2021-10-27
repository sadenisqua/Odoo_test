from odoo import models, fields, api


class SestraPolishTest(models.Model):
    _name = 'sestra.polish.test'
    _description = 'Sestra Polish Test'

    text = fields.Text()
    check1 = fields.Boolean(string='Test 1')
    check2 = fields.Boolean(string='Test 2')
    check_all = fields.Boolean(string='Select all')
    select1 = fields.Selection(selection=[('a', '1'), ('b', '2'), ('c', '3')])
    select2 = fields.Selection(selection=[('d', '4'), ('f', '5'), ('g', '6')])
    boolean1 = fields.Boolean(string='1')
    boolean2 = fields.Boolean(string='2')
    boolean3 = fields.Boolean(string='3')
    boolean4 = fields.Boolean(string='4')
    boolean5 = fields.Boolean(string='5')
    boolean6 = fields.Boolean(string='6')
    boolean7 = fields.Boolean(string='7')
    boolean8 = fields.Boolean(string='8')
    boolean9 = fields.Boolean(string='9')
    partner_id = fields.Many2one('res.partner', domain="[('is_wizzard', '=', True)]")

    @api.onchange('check_all')
    def _check_all(self):
        if self.check_all:
            self.check1 = True
            self.check2 = True
        elif not self.check_all:
            self.check1 = False
            self.check2 = False

    @api.onchange('check1')
    def _onchange_check1(self):
        if not self.text:
            self.text = " "
        if self.text and self.check1:
            self.text += f" [ {self.env['sestra.polish.test'].fields_get()['check1']['string']} ] "
        elif not self.check1:
            self.text = self.text.replace(f" [ {self.env['sestra.polish.test'].fields_get()['check1']['string']} ] ",
                                          '')

    @api.onchange('check2')
    def _onchange_check2(self):
        if not self.text:
            self.text = " "
        if self.text and self.check2:
            self.text += f" { {self.env['sestra.polish.test'].fields_get()['check2']['string']} } "
        elif not self.check2:
            self.text = self.text.replace(f" { {self.env['sestra.polish.test'].fields_get()['check2']['string']} } ",
                                          '')

    def wizzard_start(self):

        return {"type": "ir.actions.act_window",
                "res_model": "sestra.polish.test.wizzard",
                "view_mode": "form",
                "target": "new",
                "context": {"default_wizzard_text": self.text}
                }
