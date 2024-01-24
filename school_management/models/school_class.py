# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SchoolClass(models.Model):
    _name = "school.class"
    _description = "School Class"

    name = fields.Integer(string="Standard")
    section = fields.Char(string="Section")
    teacher_id = fields.Many2one('hr.employee', string="Teacher")
    student_ids = fields.One2many('school.student', 'class_id', string="Student")
