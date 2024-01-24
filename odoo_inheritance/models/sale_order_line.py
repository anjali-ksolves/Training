# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
# from odoo.fields import Command


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Float(string="Discount Amount")


    # account_move_line_id = fields.One2many('account.move.line', 'sale_order_line_ids')
    #
    # def _prepare_invoice_line(self, **optional_values):
    #     res = {
    #         'display_type': self.display_type or 'product',
    #         'sequence': self.sequence,
    #         'name': self.name,
    #         'product_id': self.product_id.id,
    #         'product_uom_id': self.product_uom.id,
    #         'quantity': self.qty_to_invoice,
    #         'discount': self.discount,
    #         'price_unit': self.price_unit,
    #         'tax_ids': [Command.set(self.tax_id.ids)],
    #         'sale_line_ids': [Command.link(self.id)],
    #         'is_downpayment': self.is_downpayment,
    #         'discount_amount': self.discount_amount,
    #     }
    #     # res['discount_amount'] = self.account_move_line_id.discount_amount
    #     return res

    # def _prepare_invoice_line(self, **optional_values):
    #     res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
    #     res.update({'discount_amount': self.discount_amount})
    #     return res
