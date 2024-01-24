# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    discount_amount = fields.Float(related='sale_line_ids.discount_amount', string="Discount Amount")
    additional_price = fields.Float(related="purchase_line_id.additional_price", string='Additional Price')

    # sale_order_line_ids = fields.Many2one('sale.order.line')