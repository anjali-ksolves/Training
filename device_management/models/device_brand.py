# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class DeviceBrand(models.Model):
    _name = 'device.brand'
    _description = 'Device Brand'

    name = fields.Char(string="Name")
    device_model_ids = fields.One2many('device.model', 'device_brand_id', string="Device Model")