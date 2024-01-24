# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class DeviceAttribute(models.Model):
    _name = 'device.attribute'
    _description = 'Device Attribute'

    name = fields.Char(string="Device Attribute Name")
    required = fields.Boolean(string="Required")
    device_type_id = fields.Many2one('device.type', string="Device Type Id")

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Name must be unique!')
    ]