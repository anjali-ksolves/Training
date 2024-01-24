# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class DeviceManagementSettings(models.TransientModel):
    _inherit = "res.config.settings"

    panel = fields.Boolean(string="Panel")

    def set_values(self):
        super(DeviceManagementSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('device', self.panel)

    @api.model
    def get_values(self):
        res = super(DeviceManagementSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(
            panel=params.get_param('device')
        )
        return res
