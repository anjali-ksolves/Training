{
    'name': "school_management",
    'summary': """School Management""",
    'description': """School Management""",
    'author': "Anjali",
    'depends': ['base', 'hr', 'web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/exam_wizard_view.xml',
        'views/teacher_view.xml',
        'views/menu.xml',
        'views/class_view.xml',
        'views/student_view.xml',
        'views/fees.xml',
        'reports/student_report.xml',
        'reports/report.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'school_management/static/src/xml/valid_email_field.xml',
    #         'school_management/static/src/js/valid_email_field.js',
    #
    #     ]
    # },
    'installable': True,
    'application': True,
    'auto_install': False,
}
# -*- coding: utf-8 -*-
