# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class DeviceBrand(models.Model):
    _name = 'device.brand'
    _description = 'Device Brand'

    name = fields.Char(string="Name")
    device_model_ids = fields.One2many('device.model', 'device_brand_id', string="Device Model")

    def create_record(self):
        self.write({'device_model_ids': [(0, 0, {'name': self.name})]})

    def update_record(self):
        self.write({
            'device_model_ids': [(1, self.id, {'name': 'Updated Name'})],
        })

    def delete_record(self):
        self.write({
            'device_model_ids': [(2, 6)]
        })

    def unlink_record(self):
        self.write({
            'device_model_ids': [(3, 3)],
        })

    def link_record(self):
        self.write({
            'device_model_ids': [(4, 7)],
        })

    # def replace_record(self):
    #     self.write({'device_model_ids': [(6, 0, [1, 2, 3])]})
