# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleButton(models.TransientModel):
    _name = "sale.order.wizard"
    _description = "Sale Order Wizard"

    sale_order_id = fields.Many2one('sale.order', string='Sale Order Id')
    custom_order_lines_wizard_id = fields.One2many('custom.order.lines.wizard', 'sale_order_line_wizard',
                                                   string="Custom Order Lines Wizard")
    total = fields.Float(string="Total", compute="_compute_total", store=True)

    @api.depends('custom_order_lines_wizard_id.subtotal')
    def _compute_total(self):
        sum = 0
        for line in self.custom_order_lines_wizard_id:
            sum += line.subtotal
        self.total = sum

    @api.model
    def default_get(self, fields):
        res = super(SaleButton, self).default_get(fields)
        active_id = self.env.context.get('active_id')
        sale_order = self.env['sale.order'].browse(active_id)
        custom_order_lines = []

        for order_line in sale_order.order_line:
            custom_order_lines.append((0, 0, {
                'product_id': order_line.product_id.id,
                'description': order_line.name,
                'quantity': order_line.product_uom_qty,
                'delivered': order_line.qty_delivered,
                'invoiced': order_line.qty_invoiced,
                'price_unit': order_line.price_unit,
                'taxes': order_line.tax_id.ids,
                'subtotal': order_line.price_subtotal,
            }))
        res['sale_order_id'] = active_id
        res['custom_order_lines_wizard_id'] = custom_order_lines
        return res

    def action_save(self):
        custom_order_lines_list = []
        for line in self.custom_order_lines_wizard_id:
            custom_order_line = self.env['custom.order.lines'].create({
                'sale_order_line': self.sale_order_id.id,
                'product_id': line.product_id.id,
                'description': line.description,
                'quantity': line.quantity,
                'delivered': line.delivered,
                'invoiced': line.invoiced,
                'price_unit': line.price_unit,
                'taxes': line.taxes.ids,
                'subtotal': line.subtotal,
            })
            custom_order_lines_list.append(custom_order_line.id)
            self.sale_order_id.write({
                'custom_order_lines_id': [(6, 0, custom_order_lines_list)],
            })

        # def action_save(self):
        #     sale_order = self.sale_order_id
        #     for rec in self.custom_order_lines_wizard_id:
        #         val = {
        #             'product_id': rec.product_id,
        #             'description': rec.description
        #         }
        #         sale_order.custom_order_lines_id = [(0, 0, val)]


class CustomOrderLinesWizard(models.TransientModel):
    _name = "custom.order.lines.wizard"
    _description = "Custom Order Lines Wizard"

    sale_order_line_wizard = fields.Many2one('sale.order.wizard', string='Sale Order Wizard')

    product_id = fields.Many2one('product.product', string="Product")
    description = fields.Text(string="Description")
    quantity = fields.Float(string="Quantity", default='1')
    delivered = fields.Float(string="Delivered")
    invoiced = fields.Float(string="Invoiced")
    price_unit = fields.Float(string="Unit Price")
    taxes = fields.Many2many('account.tax', string="Taxes")
    subtotal = fields.Float(string="Subtotal")

    @api.onchange('product_id')
    def onchange_object(self):
        for rec in self:
            rec.price_unit = self.product_id.id

    # @api.depends('price_unit', 'quantity')
    # def _compute_subtotal(self):
    #     for records in self:
    #         records.subtotal = self.quantity * self.price_unit
