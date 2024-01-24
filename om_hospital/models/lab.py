# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HospitalLab(models.Model):
    _name = "hospital.lab"
    _description = "Hospital Laboratory"

    name = fields.Char(string='Name', required=True)
    user_id = fields.Many2one('res.users', string="Responsible")

    @api.model
    def default_get(self, fields):
        val = {'user_id': self.env.user.id}
        return val
