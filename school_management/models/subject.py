# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Subject(models.Model):
    _name = "school.subject"
    _description = "School Subject"

    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")
    student_subject_id = fields.Many2many('school.student')
    subject_wizard_ids = fields.One2many('school.subject.wizard', 'subject_id', string="Subject Wizard")
