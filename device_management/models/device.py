# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Device(models.Model):
    _name = 'device'
    _description = 'Device'

    name = fields.Char(string="Name")
    shared = fields.Boolean(string="Shared")
    device_model_id = fields.Many2one('device.model', string="Device Model")
    device_type_id = fields.Many2one('device.type', string="Device Type")
    device_brand_id = fields.Many2one('device.brand', string="Device Brand")
    customer_rating = fields.Integer(string="Customer Rating")

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Name must be unique!')
    ]
