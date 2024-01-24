# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    custom_invoice_id = fields.One2many('custom.invoice', 'account_move_id', string="Custom Invoice")
    # total = fields.Float(string="Total", compute="_compute_total", store=True)

    # @api.depends('custom_invoice_id.subtotal')
    # def _compute_total(self):
    #     sum = 0
    #     for line in self.custom_invoice_id:
    #         sum += line.subtotal
    #     self.total = sum


class CustomInvoice(models.Model):
    _name = "custom.invoice"
    _description = "Custom Invoice"
    _auto = False

    account_move_id = fields.Many2one('account.move', string="Account Move")

    product_id = fields.Many2one('product.product', string="Product")
    description = fields.Text(string="Description")
    quantity = fields.Float(string="Quantity", default='1')
    delivered = fields.Float(string="Delivered")
    invoiced = fields.Float(string="Invoiced")
    price_unit = fields.Float(string="Unit Price")
    taxes = fields.Many2many('account.tax', 'account_tax_custom_invoice_rel_2', 'cust_id', 'rel_id', string="Taxes")
    subtotal = fields.Float(string="Subtotal")

    # @api.onchange('product_id')
    # def onchange_object(self):
    #     for rec in self:
    #         rec.price_unit = self.product_id.id

    @api.depends('price_unit', 'quantity')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = self.quantity * self.price_unit

