# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ExamWizard(models.TransientModel):
    _name = 'school.exam.wizard'
    _description = 'Exam Wizard'

    student_name = fields.Many2one('school.student', string="Student Name")
    exam_ids = fields.Many2one('school.exam', string="School Exam")
    sw_ids = fields.One2many('school.subject.wizard', 'ew_id', string="Subject Wizard")

    def default_get(self, fields):
        res = super(ExamWizard, self).default_get(fields)
        active_id = self.env.context.get('active_id')
        student_details = self.env['school.student'].browse(active_id)
        information = []

        for line in student_details.subject_id:
            information.append((0, 0, {
                'sub': line.name,
            }))
            print(line.name)

        res['sw_ids'] = information
        res['student_name'] = student_details.name
        return res

    def action_save(self):
        active_id = self.env.context.get('active_id')
        s_rec = self.env['school.student'].browse(active_id)
        s_rec.exam_ids.unlink()
        for rec in self.sw_ids:
            val = {
                'subject': rec.sub,
                'marks': rec.marks,
                'out_of': rec.out_of
            }
            print(val)
            s_rec.exam_ids = [(0, 0, val)]
            # s_rec.exam_ids.student_id = self.student_name


class SubjectWizard(models.TransientModel):
    _name = 'school.subject.wizard'
    _description = 'Subject Wizard'

    subject_id = fields.Many2one('school.subject', string="Subject Name")
    student_name = fields.Char(string="Student")
    sub = fields.Char(string="Stream")
    ew_id = fields.Many2one('school.exam.wizard', string="Exam Wizard")
    marks = fields.Float(string="Marks")
    out_of = fields.Float(string="Total Marks", default='100')
