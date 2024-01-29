# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError
import psycopg2


class Student(models.Model):
    _name = "school.student"
    _description = "School Student"

    name = fields.Char(string="Student name")
    subject_id = fields.Many2many('school.subject')
    exam_ids = fields.One2many('school.exam', 'student_id', string="Exam")
    exam_wizard = fields.One2many('school.exam.wizard', 'student_name', string="Exam Wizard")
    father = fields.Char(string='Father')
    mother = fields.Char(string='Mother')
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")
    address = fields.Text(string='Correspondence Address')
    father_occupation = fields.Char(string="Father's occupation")
    mother_occupation = fields.Char(string="Mother's occupation")
    contact = fields.Integer(string="Contact")
    email = fields.Char(string="Email")
    class_id = fields.Many2one('school.class', string="Class")
    teacher_id = fields.Many2many('hr.employee', string="Teacher")
    fees_id = fields.One2many('school.fees', 'student_ids', string="Fees")
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm')], default='draft',
                             string="Status")

    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.dob:
                rec.age = today.year - rec.dob.year
            else:
                rec.age = 0

    def action_confirm(self):
        self.state = 'confirm'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    def action_db(self):
        database1_connection = psycopg2.connect(
            host='localhost',
            port='5432',
            user='odoo',
            password='odoo',
            dbname='ksolves'
        )
        database1_cursor = database1_connection.cursor()
        try:
            database1_cursor.execute('INSERT INTO school_student (name,gender) VALUES (%s,%s)', (self.name, self.gender))
            self.env['school.student'].create({'name': self.name, 'gender': self.gender})
            database1_connection.commit()
        finally:
            database1_connection.close()
