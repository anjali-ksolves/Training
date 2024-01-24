from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    custom_purchase_lines_id = fields.One2many('custom.purchase.lines', 'purchase_order_line',
                                               string="Custom Purchase Lines")

    def pass_value(self):
        self.custom_purchase_lines_id.unlink()
        print("Hello")
        for rec in self.order_line:
            custom_purchase = {
                'product_id': rec.product_id.id,
                'description': rec.name,
                'qty': rec.product_qty,
                'price_unit': rec.price_unit,
                'subtotal': rec.price_subtotal
            }
            print(custom_purchase)
            self.custom_purchase_lines_id = [(0, 0, custom_purchase)]

    def action_send_mail(self):
        mail = self.env['mail.mail']
        values = {
            'email_from': 'anjali.thakur@ksolves.com',
            'email_to': 'hrishabh.nagar@ksolves.com',
            'body_html': 'Test mail',
        }
        mail_rec = mail.create(values)
        mail_rec.send()
        print("Mail Sent!!!!!!!!!!!!!!!!!")

    # @api.model
    # def default_get(self):
    #     res = super(PurchaseOrder, self).default_get(fields)
    #     active_id = self.env.context.get('active_id')
    #     purchase_order = self.env['purchase.order'].browse(active_id)
    #     purchase_lines = []
    #
    #     for order_line in purchase_order.order_line:
    #         purchase_lines.append((0, 0, {
    #             'product_id': order_line.product_id.id,
    #             'description': order_line.name,
    #             'qty': order_line.product_qty,
    #             'received': order_line.qty_received,
    #             'billed': order_line.qty_invoiced,
    #             'uom': order_line.product_uom.id,
    #             'price_unit': order_line.price_unit,
    #             'taxes': order_line.taxes_id.id,
    #             'subtotal': order_line.price_subtotal,
    #         }))
    #     res['custom_purchase_lines_id'] = purchase_lines
    #     return res


class CustomPurchaseLines(models.Model):
    _name = "custom.purchase.lines"
    _description = "Custom Purchase Lines"

    purchase_order_line = fields.Many2one('purchase.order', string='Purchase Order')

    product_id = fields.Many2one('product.product', string="Product")
    description = fields.Text(string="Description")
    qty = fields.Float(string="Quantity", default='1')
    received = fields.Float(string="Received")
    billed = fields.Float(string="Billed")
    uom = fields.Many2one('uom.uom', string="UoM")
    price_unit = fields.Float(string="Unit Price")
    taxes = fields.Many2many('account.tax', string="Taxes")
    subtotal = fields.Float(string="Subtotal")

    # @api.depends('price_unit')
    # def _compute_total(self):
    #     for records in self.purchase_order_line:
    #         records.subtotal = self.qty * self.price_unit


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    additional_price = fields.Float(string="Additional Price")
