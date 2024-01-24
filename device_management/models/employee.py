# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Employee(models.Model):
    _inherit = 'hr.employee'

    device_assignment_id = fields.One2many('device.assignment', 'emp_id', string="Device Assignment")