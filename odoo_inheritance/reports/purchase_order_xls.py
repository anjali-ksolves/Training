import base64
import io
from odoo import models

class PurchaseOrderXlsx(models.AbstractModel):
    _name = 'report.odoo_inheritance.purchase_order_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        bold = workbook.add_format({'bold':True})
        # format_1 = workbook.add_format({'align': 'center', 'bg-color': 'yellow', 'font_size': 14})
        # format_2 = workbook.add_format({'align': 'center', 'font_size': 10})
        sheet = workbook.add_worksheet('Product Order Excel')
        # sheet.write(2, 2, 'Product', format_1)
        # sheet.write(2, 3, lines.product_id, format_2)
        # sheet.write(3, 2, 'Description', format_1)
        # sheet.write(3, 3, lines.name, format_2)
