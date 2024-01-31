# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date


class DeviceAssignment(models.Model):
    _name = 'device.assignment'
    _description = 'Device Assignment'

    name = fields.Char(string="Device Assignment Name")
    date_start = fields.Date(string="Start Date")
    date_expire = fields.Date(string="Expire Date")
    state = fields.Selection([('new', 'New'), ('draft', 'Draft'), ('approved', 'Approved'), ('returned', 'Returned'),
                              ('rejected', 'Rejected')], string="State")
    emp_id = fields.Many2one('hr.employee', string="Employee")

    change = fields.Boolean(string="Change", compute="change_visibility")

    def insert_name(self):
        query = """
        insert into device_assignment(name) values('anjali');
        """
        self.env.cr.execute(query)

    def select_query(self):
        query = """
         select name from device_assignment where name = '%s';
         """ % (self.name)
        self.env.cr.execute(query)
        values = self.env.cr.dictfetchall()
        print("values------>", values)

    def update_query(self):
        query = """
            update device_assignment set state='approved' where name='anjali';
            """
        self.env.cr.execute(query)

    def delete_query(self):
        query = """
        delete from device_assignment where name = 'anjali';
        """
        self.env.cr.execute(query)

    # _sql_constraints = [
    #     ('unique_name', 'unique(name)', 'Name must be unique!')
    # ]

    @api.depends('change')
    def change_visibility(self):
        res = self.env['ir.config_parameter'].get_param('device')
        self.change = res

    def check_rpc(self):
        print("--------------");
        for records in self:
            records.state = 'approved'



