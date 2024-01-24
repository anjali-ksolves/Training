# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Exam(models.Model):
    _name = "school.exam"
    _description = "School Exam"

    student_id = fields.Many2one('school.student', string="Student")
    subject = fields.Char(string="Subject")
    marks = fields.Float(string="Marks")
    out_of = fields.Float(string="Total Marks")
    exam_wizard_ids = fields.One2many('school.exam.wizard', 'exam_ids', string="Exam Wizard")




