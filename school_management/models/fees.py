# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Fees(models.Model):
    _name = "school.fees"
    _description = "School Fees"

    month = fields.Selection([('january', 'January'),
                              ('february', 'February'),
                              ('march', 'March'),
                              ('april', 'April'),
                              ('may', 'May'),
                              ('june', 'June'),
                              ('july', 'July'),
                              ('august', 'August'),
                              ('september', 'September'),
                              ('october', 'October'),
                              ('november', 'November'),
                              ('december', 'December')
                              ], string="Month")

    total_fees = fields.Float(string="Total Fees")
    paid = fields.Float(string="Paid")
    remaining = fields.Float(string="Remaining Fees")
    student_ids = fields.Many2one('school.student', string="Student")

    # _sql_constraints = [
    #     ('unique_month', 'unique(month)', 'Month should be unique!')
    # ]