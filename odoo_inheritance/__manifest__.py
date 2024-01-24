# -*- coding: utf-8 -*-
{
    'name': "odoo_inheritance",
    'summary': """Odoo Inheritance""",
    'description': """Odoo Inheritance""",
    'author': "Anjali",
    'website': "https://www.yourcompany.com",
    'version': '0.1',
    'depends': ['base', 'sale', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/sale_button_view.xml',
        'views/sale_order_view.xml',
        'views/custom_invoice.xml',
        'views/purchase_order.xml',
        'reports/purchase_order_template.xml',
        'reports/report.xml',
        # 'data'/'mail_template_data.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
