# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class DeviceType(models.Model):
    _name = 'device.type'
    _description = 'Device Type'

    name = fields.Char(string="Device Type Name")
    code = fields.Char(string="Code")
    sequence = fields.Integer(string="Sequence", default=lambda self: self.env['ir.sequence'].next_by_code('device.type') or '',)
    device_attribute_ids = fields.One2many('device.attribute', 'device_type_id', string="Device Attribute Ids")
    device_model_ids = fields.One2many('device.model', 'model_device_type_id', string="Device Model Ids")
    # active = fields.Boolean(string="IsActive")

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Name must be unique!'),
        ('unique_code', 'unique(code)', 'Code must be unique!')
    ]

    # @api.model
    # def create(self, vals):
        # if 'sequence' in vals and vals['sequence'] == _(1):
        #     sequence_value = int(self.env['ir.sequence'].next_by_code('device.type'))
        #     vals['sequence'] = sequence_value
        # res = super(DeviceType, self).create(vals)
        # return res
