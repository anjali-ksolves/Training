# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class DeviceModel(models.Model):
    _name = 'device.model'
    _description = 'Device Model'

    name = fields.Char(string="Device Model Name")
    model_device_type_id = fields.Many2one('device.type', string="Device Type Id")
    device_brand_id = fields.Many2one('device.brand', string="Device Brand")

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Name must be unique!')
    ]