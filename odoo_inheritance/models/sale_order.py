# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.fields import Command


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')
    custom_order_lines_id = fields.One2many('custom.order.lines', 'sale_order_line', string="Custom Order Lines")

    custom_bills = fields.Many2one('custom.invoice', string='Custom Invoice')
    total = fields.Float(string="Total", compute="_compute_total", store=True)

    @api.depends('custom_order_lines_id.subtotal')
    def _compute_total(self):
        sum = 0
        for line in self.custom_order_lines_id:
            sum += line.subtotal
        self.total = sum

    def send_bill(self):
        invoices = self.mapped('invoice_ids')
        invoices.custom_invoice_id.unlink()
        for rec in self.custom_order_lines_id:
            sale_bill = {
                'product_id': rec.product_id.id,
                'description': rec.description,
                'quantity': rec.quantity,
                'delivered': rec.delivered,
                'invoiced': rec.invoiced,
                'price_unit': rec.price_unit,
                'taxes': rec.taxes,
                'subtotal': rec.subtotal,
            }
            invoices.custom_invoice_id = [(0, 0, sale_bill)]


class CustomOrderLines(models.Model):
    _name = "custom.order.lines"
    _description = "Custom Order Lines"

    sale_order_line = fields.Many2one('sale.order', string='Sale Order')

    product_id = fields.Many2one('product.product', string="Product")
    description = fields.Text(string="Description")
    quantity = fields.Float(string="Quantity", default=1.0)
    delivered = fields.Float(string="Delivered")
    invoiced = fields.Float(string="Invoiced")
    price_unit = fields.Float(string="Unit Price")
    taxes = fields.Many2many('account.tax', string="Taxes")
    subtotal = fields.Float(string="Subtotal", compute="_compute_subtotal", store=True)

    @api.onchange('product_id')
    def onchange_object(self):
        for rec in self:
            rec.price_unit = self.product_id.id

    @api.depends('price_unit', 'quantity')
    def _compute_subtotal(self):
        for records in self:
            records.subtotal = self.quantity * self.price_unit
