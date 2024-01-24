# -*- coding: utf-8 -*-
import contextlib
from odoo import fields, models, api, sql_db, SUPERUSER_ID


class Teacher(models.Model):
    _inherit = 'hr.employee'

    teacher_id = fields.Many2many('school.student', 'school_teacher_rel', 'tid', 'sid', string="Teacher")
    class_ids = fields.One2many('school.class', 'teacher_id', string="Class Lines")
    # class_line = fields.Many2many('teacher.class', 'class_teacher', 'cid', 'tid', string="ClassId")
    subject_name = fields.Many2one('odoo.subject', string="Subject")

    def action_confirm(self):
        connection = sql_db.db_connect('newnewnew')
        with contextlib.closing(connection.cursor()) as cr:
            cr.autocommit(True)
            env = api.Environment(cr, SUPERUSER_ID, {})
            env['hr.employee'].create({'name': self.name, 'work_email': self.work_email})

    def create_duplicate(self):
        self.env['hr.employee'].create({'name': self.name, 'work_email': self.work_email})

    def action_update(self):
        connection = sql_db.db_connect('odoo_16_4')
        with contextlib.closing(connection.cursor()) as cr:
            cr.autocommit(True)
            env = api.Environment(cr, SUPERUSER_ID, {})
            env['hr.employee'].write({'work_email': self.work_email})

