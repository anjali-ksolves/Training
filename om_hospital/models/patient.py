# -*- coding: utf-8 -*-

from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"

    image = fields.Binary(string="Profile Photo")
    name = fields.Char(string='First Name', tracking=True)
    last_name = fields.Char(string='Last Name', tracking=True)
    ref = fields.Integer(string='Reference', compute="_compute_ref")
    date_of_birth = fields.Date(string="Date of Birth", tracking=True)
    age = fields.Integer(string="Age", compute="_compute_age", tracking=True, store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    blood_group = fields.Char(string="Blood_group", tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    pharmacy_line_ids = fields.One2many('patient.pharmacy.lines', 'patient_id', string='Pharmacy Lines')
    attachments = fields.Binary(string="Documents", attachment=True, tracking=True)
    total = fields.Float(string="Total", compute="_compute_total", store=True)
    doctor_id = fields.Many2one('res.partner', required=True)
    contact = fields.Char(related='doctor_id.phone', tracking=True)
    email = fields.Char(related='doctor_id.email', tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('cancel', 'Cancel')], default='draft',
                             string="Status", tracking=True)

    @api.depends('pharmacy_line_ids.price_unit')
    def _compute_total(self):
        for line in self:
            for records in self.pharmacy_line_ids:
                line.total += records.price_unit

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    @api.depends('ref')
    def _compute_ref(self):
        rec = 0
        for record in self:
            rec = rec + 1
            record.ref = rec

    def action_confirm(self):
        self.state = 'confirm'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    def action_doctor(self):
        doctor_id = self.doctor_id
        contact = self.contact
        email = self.email
        return {
            'type': 'ir.actions.act_window',
            'name': 'Doctors',
            'res_model': 'res.partner',
            'res_id': doctor_id.id,
            'view_mode': 'form',
            'view_id': self.env.ref('base.view_partner_form').id,
            'target': 'current'
        }

    @api.depends('pharmacy_line_ids.medicine_id')
    def onchange_object(self):
        for rec in self:
            rec.price_unit = self.pharmacy_line_ids.medicine_id

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("The entered date of birth is not acceptable !"))

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'Name must be unique!')
    ]


class PatientPharmacyLines(models.Model):
    _name = "patient.pharmacy.lines"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Patient Pharmacy Lines"

    medicine_id = fields.Many2one('patient.medicines', string='Medicines')
    price_unit = fields.Float(string='Price')
    qty = fields.Integer(string='Quantity', default=1)
    patient_id = fields.Many2one('hospital.patient', string='Patient')
    total = fields.Float(string='Total')


class Medicines(models.Model):
    _name = "patient.medicines"
    _description = "Patient Medicines"

    name = fields.Char(string='Medicines')
    list_price = fields.Integer(string='Price')
    expiry_date = fields.Date(string="Expiry Date")
