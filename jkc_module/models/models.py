# -*- coding: utf-8 -*-

from odoo import models, fields, api


class jkc_module(models.Model):
    _name = 'jkc_module'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100


class HospitalPartner(models.Model):
    # _name = 'res.partner_ext11'
    _inherit = 'res.partner'

    tbeds = fields.Integer()
    vents = fields.Integer()
    meds = fields.Integer()
    cbeds = fields.Integer()
    ask = fields.Text()
    contact_type = fields.Text()
